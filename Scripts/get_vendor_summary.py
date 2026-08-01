import pandas as pd
import logging
import os
import numpy as np                 
from sqlalchemy import create_engine 
from Ingestion_db import ingest_db

path = "."

# Reset and configure loggers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def create_vendor_summary(engine):
    """Extract data from PostgreSQL using exact case-sensitive matching."""
    vendor_sales_summary = pd.read_sql_query(""" 
    WITH freight_summary AS (
        SELECT 
            "VendorNumber", 
            SUM("Freight") as frieght_cost
        FROM vendor_invoice
        GROUP BY "VendorNumber"
    ),

    purchase_summary AS (
        SELECT 
            p."VendorName",
            p."VendorNumber",
            p."Brand", 
            p."Description",
            p."PurchasePrice", 
            SUM(p."Quantity") as total_purchase_qantity, 
            SUM(p."Dollars") as total_purchase_dollars,
            pp."Volume",
            pp."Price" as actual_price
        FROM Purchases p
        JOIN "purchase_prices" pp ON p."Brand" = pp."Brand"
        WHERE p."PurchasePrice" > 0
        GROUP BY p."VendorNumber", p."VendorName", p."Brand", p."Description", p."PurchasePrice", pp."Price", pp."Volume"
    ),

    sales_summary AS (
        SELECT 
            "VendorNo" AS sales_vendor_id, 
            "Brand",
            SUM("SalesDollars") as total_sales_dollar,
            SUM("SalesPrice") as total_sales_price,
            SUM("SalesQuantity") as total_sales_quantity,
            SUM("ExciseTax") as total_excise_tax
        FROM sales
        GROUP BY "VendorNo", "Brand"
    )

    SELECT
        ps."VendorNumber",
        ps."VendorName", 
        ps."Brand",
        ps."Description",
        ps."PurchasePrice",
        ps.actual_price,
        ps."Volume",
        ss.total_sales_dollar,
        ss.total_sales_price,
        ss.total_sales_quantity,
        ss.total_excise_tax,
        ps.total_purchase_qantity,
        ps.total_purchase_dollars,
        fs.frieght_cost
    FROM purchase_summary ps
    LEFT JOIN sales_summary ss
        ON ps."VendorNumber" = ss.sales_vendor_id
        AND ps."Brand" = ss."Brand"
    LEFT JOIN freight_summary fs
        ON ps."VendorNumber" = fs."VendorNumber"
    ORDER BY ps.total_purchase_dollars DESC;
    """, engine) 

    return vendor_sales_summary

def clean_data(df):
    """Clean data and safely handle mathematical metrics for PostgreSQL precision types."""
    #Fix: Renamed local updates inside the function to use 'df' instead of 'vendor_sales_summary'
    df['Volume'] = df['Volume'].astype('float64')
    
    #Strip spaces from categorical columns
    df['VendorName'] = df['VendorName'].astype(str).str.strip()

    # Create new financial columns for metrics analysis
    df['gross_profit'] = df['total_sales_dollar'] - df['total_purchase_dollars']
    df['profit_margin'] = (df['gross_profit'] / df['total_sales_dollar']) * 100
    df['stock_turnover'] = df['total_sales_quantity'] / df['total_purchase_qantity']
    df['sales_purchase_ratio'] = df['total_sales_dollar'] / df['total_purchase_dollars']

    # Fix: Convert infinite values (division by zero results) to zero before Postgres upload
    df.replace([np.inf, -np.inf], 0, inplace=True)
    
    # Fill remaining empty / missing cells cleanly with zero
    df.fillna(0, inplace=True)

    return df

if __name__ == '__main__':
    # 🔑 Update connection config with your local PostgreSQL user details
    DATABASE_URL = "postgresql+psycopg2://postgres:history123@localhost:5432/Inventory_db"
    engine = create_engine(DATABASE_URL)

    logging.info('Starting vendor summary tracking process--------')
    summary_df = create_vendor_summary(engine)
    logging.info(f"Extracted shape: {summary_df.shape}")

    logging.info('Cleaning data and fixing infinity structures................')
    clean_df = clean_data(summary_df)
    logging.info(f"Cleaned head sample: \n{clean_df.head(2)}")

    logging.info('Ingesting final data to PostgreSQL database.............')
    # 🔑 Assuming your custom ingest_db handles engine connections or raw parameters
    ingest_db(clean_df, 'vendor_sales_summary', engine)
    logging.info('ETL Pipeline Processing Completed successfully!')