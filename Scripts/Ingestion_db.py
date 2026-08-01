import pandas as pd
import os
import io
import logging

os.makedirs("Logs", exist_ok =True)

#config the loging 
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(message)s", #takes time from computer time automatically
    handlers=[
        logging.FileHandler(
            "logs/pipeline.log"
        ),
        logging.StreamHandler(),
    ],
)


def ingest_db(df, table_name,  engine):
    df.columns = df.columns.str.strip()
    logging.info(f"starting database creation for table: '{table_name}'")

    #using native postgres command to better optimize the code for larger datasets
    try:
        df.head(0).to_sql(table_name, con = engine, if_exists = 'replace' , index = False)
        raw_conn = engine.raw_connection()
        with raw_conn.cursor() as cursor:
            output = io.StringIO()
            df.to_csv(output, sep=',',header = False, index = False)
            output.seek(0)
            
            sql = f"COPY {table_name} FROM STDIN WITH CSV DELIMITER ','"
            cursor.copy_expert(sql, output)
            raw_conn.commit()
            print(f" {table_name} imported successfully")
            logging.info( f"success: '{table_name}' imported ")
    except Exception as e:
        print(f"ERROR importing {table_name}: {e}")
        logging.error( f"failed: '{table_name}' imported ")

    finally:
        raw_conn.close()

    #Run your file through loop
def load_raw_data():
    for file in os.listdir('.'):
        if '.csv' in file:
            table_name = file[:-4]
            try: 
                logging.info(f"reading file '{file}'")
                df = pd.read_csv(file)
                ingest_db(df, file[:-4], engine)
            except Exception as e:
                logging.error(f" failed to read '{file}':{e}")
logging.info("data ingestion pipeline finished")
if __name__ == '__main__':
    load_raw_data()