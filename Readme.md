# 📊 Vendor Performance Analysis

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter)

---

## 📖 Project Overview

Vendor Performance Analysis is an end-to-end data analytics project that analyzes purchasing, inventory, and vendor transaction data to uncover business insights and evaluate vendor efficiency.

The project demonstrates the complete analytics workflow from importing raw CSV files into PostgreSQL to performing exploratory data analysis (EDA), SQL-based querying, and generating actionable business insights using Python.

---

## 🎯 Objectives

- Import vendor datasets into PostgreSQL
- Connect Python with PostgreSQL using SQLAlchemy
- Clean and preprocess the data
- Perform Exploratory Data Analysis (EDA)
- Analyze vendor purchasing and inventory trends

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python |
| Database | PostgreSQL |
| Query Language | SQL |
| Libraries | Pandas, NumPy, SQLAlchemy, Psycopg2 |
| Visualization | Matplotlib, Seaborn |
| IDE | Jupyter Notebook |

---

## 📂 Repository Structure

```
Vendor_Performance_Analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── ingestion_1.ipynb
│   ├── Vendor_analysis_connection.ipynb
│   ├── Exploratory data analysis.ipynb
│   └── vendor_performance_analysis.ipynb
│
├── images/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🔄 Project Workflow

```
Raw CSV Files
       │
       ▼
Data Ingestion
       │
       ▼
PostgreSQL Database
       │
       ▼
Data Cleaning
       │
       ▼
Exploratory Data Analysis
       │
       ▼
Business Insights
```

---

## 📊 Exploratory Data Analysis

The project performs:

- Dataset inspection
- Missing value analysis
- Summary statistics
- Distribution analysis
- Correlation analysis
- Outlier detection
- Vendor-wise analysis
- Inventory analysis
- Purchase trend analysis

---

## 🗄️ Database Integration

PostgreSQL is used as the backend database.

The project demonstrates:

- Creating database connections
- Loading CSV files into PostgreSQL
- Executing SQL queries
- Reading data into Pandas
- Query optimization using SQLAlchemy

---

## 📈 Visualizations

The analysis includes various visualizations such as:

- Distribution plots
- Box plots
- Histograms
- Correlation heatmaps
- Vendor comparison charts
- Purchase trend analysis



Example:

```markdown
![Summary Statistics](images/Screenshot 2026-08-01 160317.png)
```

---

## 💡 Key Insights

The project explores:

- Vendor purchasing performance
- Inventory distribution
- Purchase cost trends
- Product-wise analysis
- Vendor comparisons
- Business performance metrics

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/Vendor_Performance_Analysis.git
```

### Navigate to the Project

```bash
cd Vendor_Performance_Analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure PostgreSQL

Update the database credentials inside the notebooks:

```python
DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/database_name"
```

### Run the notebooks in order

1. `ingestion_1.ipynb`
2. `Vendor_analysis_connection.ipynb`
3. `Exploratory data analysis.ipynb`
4. `vendor_performance_analysis.ipynb`

---

## 📁 Dataset

The project uses vendor purchasing and inventory datasets stored in CSV format.

> **Note:** If the dataset is proprietary or unavailable for redistribution, please provide a brief description instead of uploading it.

---

## 📚 Skills Demonstrated

- Data Cleaning
- Data Wrangling
- SQL
- PostgreSQL
- SQLAlchemy
- Exploratory Data Analysis
- Data Visualization
- Business Analytics
- Python Programming

---

## 🔮 Future Improvements

- Interactive Power BI Dashboard
- Automated ETL Pipeline
- Predictive Analytics
- Vendor Performance Scoring Model
- Streamlit Dashboard Deployment

---

## 🤝 Acknowledgment

This project was developed with help of a youtube video project for learning and portfolio purposes to strengthen practical skills in SQL, PostgreSQL, Python, and data analytics.

---

## 👨‍💻 Author

**Ruchir Saraf**

- LinkedIn: *(https://www.linkedin.com/in/ruchirsaraf/)*
- GitHub: *(https://github.com/Devshadow-ui)*

---
