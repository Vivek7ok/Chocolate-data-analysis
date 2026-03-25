# 🍫 Chocolate Sales Analytics Project

A full-stack data analytics pipeline for a global chocolate retail business — covering data ingestion, exploratory analysis, SQL business queries, and interactive Power BI dashboards.

---

## 📁 Project Structure

```
chocolate-sales/
│
├── Data/
│   ├── customers.csv        # 50,000 customer records
│   ├── products.csv         # 200 products across 5 categories & 6 brands
│   ├── stores.csv           # 100 stores across 6 countries
│   ├── calendar.csv         # 731-day date dimension (2023–2024)
│   └── sales.csv            # Transactional fact table
│
├── Data_insart.py           # ETL script — loads CSVs into MySQL
├── EDA.py                   # Exploratory Data Analysis & visualisations
├── query.sql                # 5 business intelligence SQL queries
└── Data_set_14.pbix         # Power BI interactive dashboard
```
 
---

## 🗄️ Database Schema

Star schema with `sales` as the central fact table.

```
customers ──┐
products  ──┤──► sales (fact)
stores    ──┤
calendar  ──┘
```

| Table      | Rows        | Key Columns                                              |
|------------|-------------|----------------------------------------------------------|
| customers  | 50,000      | customer_id, age, gender, loyalty_member, join_date      |
| products   | 200         | product_id, product_name, brand, category, cocoa_percent |
| stores     | 100         | store_id, store_name, city, country, store_type          |
| calendar   | 731         | date, year, month, day, week, day_of_week                |
| sales      | Transactional | order_id, customer_id, product_id, store_id, order_date, revenue, profit |

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.8+
- MySQL 8.x
- Power BI Desktop (for `.pbix` file)

### Install Python Dependencies

```bash
pip install pandas sqlalchemy pymysql matplotlib seaborn numpy
```

### Configure Database

Create the database in MySQL before running the ETL script:

```sql
CREATE DATABASE chocolate_sales;
```

Update the connection string in `Data_insart.py` with your credentials:

```python
conn = create_engine('mysql+pymysql://<user>:<password>@127.0.0.1:3306/chocolate_sales')
```

### Run ETL Pipeline

```bash
python Data_insart.py
```

This loads all five CSV files into MySQL. Tables are replaced on each run (idempotent).

### Run EDA

```bash
python EDA.py
```

---

## 📊 Exploratory Data Analysis

`EDA.py` merges all tables into a single denormalised flat file and produces five visualisations:

| # | Chart | Business Question |
|---|-------|-------------------|
| 1 | Revenue by Category × Country (bar) | Which categories dominate in each market? |
| 2 | Revenue by Country × Gender (bar) | Are purchasing patterns gender-differentiated? |
| 3 | Total Revenue by Year (line) | Is the business growing year-on-year? |
| 4 | Order Count by Year (line) | Is volume growing independently of revenue? |
| 5 | Loyalty Members by Country (count) | Where is the loyalty programme strongest? |

---

## 🔍 SQL Business Queries

Five production-ready queries in `query.sql`:

### Q1 — Product Revenue & Profit Margin Ranking
Ranks all products by total revenue and computes aggregate profit margins to identify top performers.

### Q2 — Seasonal Demand Analysis
Tags transactions against Valentine's Day (Feb 14) and Christmas (Dec 25) to quantify seasonal revenue spikes vs baseline.

### Q3 — Category Over/Underperformance
Uses a two-step CTE to benchmark each product against its category average, flagging over- and underperforming SKUs.

### Q4 — Channel Revenue Contribution
Applies a window function (`SUM() OVER()`) to calculate each store type's percentage share of total revenue in a single pass.

### Q5 — Average Order Value Per Customer Over Time
Tracks per-customer AOV year-on-year to reveal premiumisation trends and purchasing behaviour shifts.

---

## 📦 Dataset Overview

| Dimension        | Detail                                              |
|------------------|-----------------------------------------------------|
| Customers        | 50,000 · Ages 18–70 · 50.5% Male · 50.2% Loyalty   |
| Products         | 200 SKUs · 5 categories · 6 brands                 |
| Categories       | Truffle, Praline, Dark, Milk, White                 |
| Brands           | Mars, Cadbury, Hershey, Ferrero, Godiva, Lindt      |
| Stores           | 100 locations · Retail, Mall, Airport, Online       |
| Countries        | Canada, France, UK, USA, Australia, Germany         |
| Time Period      | Jan 2023 – Dec 2024 (731 days)                      |

---

## 📈 Power BI Dashboard

Open `Data_set_14.pbix` in Power BI Desktop for interactive exploration. The dashboard connects to the same MySQL schema and includes filters for country, channel, year, and product category.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is for educational and analytical purposes. Dataset is synthetic.

---

*Chocolate Sales Co. — Data Analytics Division · Fiscal 2023–2024*
