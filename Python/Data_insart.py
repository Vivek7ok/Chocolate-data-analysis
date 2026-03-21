import pandas as pd
from sqlalchemy import create_engine

# Create connection
conn = create_engine('mysql+pymysql://root:Vivek%40123@127.0.0.1:3306/chocolate_sales')

# 🔹 Function to load and insert data
def load_table(file_path, table_name):
    try:
        # Load CSV
        df = pd.read_csv(file_path)

        # Clean column names
        df.columns = df.columns.str.replace(' ', '_')

        # Insert into MySQL
        df.to_sql(
            table_name,
            conn,
            index=False,
            if_exists='replace',
            chunksize=1000,
            method='multi'
        )

        print(f"✅ {table_name} inserted successfully!")

    except Exception as e:
        print(f"❌ Error inserting {table_name}: {e}")


# 🔥 Load all tables one by one

load_table(r"D:\Data_set\Data_set_14\Data\customers.csv","sales")
load_table(r"D:\Data_set\Data_set_14\Data\customers.csv", "customers")
load_table(r"D:\Data_set\Data_set_14\Data\calendar.csv", "calendar")
load_table(r"D:\Data_set\Data_set_14\Data\products.csv", "products")
load_table(r"D:\Data_set\Data_set_14\Data\stores.csv", "stores")

print("\n🎯 All tables inserted successfully!")

