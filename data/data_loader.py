import pandas as pd
import sqlite3
import os

# Configuration
DB_NAME = 'sales_analysis.db'
CSV_FILE = 'FINAL_DATASET.csv'  # Make sure this path is correct relative to your script

# 1. Load Data
if not os.path.exists(CSV_FILE):
    print(f"Error: CSV file '{CSV_FILE}' not found.")
    exit()

df = pd.read_csv(CSV_FILE)
print(f"Loaded {len(df)} rows from CSV.")

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Enable Foreign Key support in SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

try:
    # 2. Execute your schema creation script
    # Ensure queries.sql is in the same directory or provide full path
    with open('queries.sql', 'r') as f:
        cursor.executescript(f.read())
    print("Schema created successfully.")

    # 3. Populate Product_Lookup
    # Extract unique product info
    products = df[['product_id', 'product_name', 'category']].drop_duplicates()
    products.to_sql('Product_Lookup', conn, if_exists='append', index=False, method='multi')
    print(f"Populated Product_Lookup with {len(products)} unique products.")

    # 4. Populate Branch_Lookup
    # Extract unique branch info
    branches = df[['branch_id', 'branch_name']].drop_duplicates()
    branches.to_sql('Branch_Lookup', conn, if_exists='append', index=False, method='multi')
    print(f"Populated Branch_Lookup with {len(branches)} unique branches.")

    # 5. Populate Sales_Transactions
    # Remove columns that are now in lookup tables
    transaction_cols = [
        'order_id', 'product_id', 'branch_id', 'date', 'day_of_week', 'month', 
        'price', 'total_sales', 'online_sales', 'offline_sales', 'returns_count', 
        'promotion_flag', 'festival_flag', 'holiday_flag', 'seasonal_index', 'cpi', 
        'lag_1', 'lag_7', 'lag_30', 'rolling_mean_7', 'rolling_mean_30'
    ]
    transactions = df[transaction_cols]
    
    # Use if_exists='append' to respect the schema we just created
    transactions.to_sql('Sales_Transactions', conn, if_exists='append', index=False, method='multi')
    print(f"Populated Sales_Transactions with {len(transactions)} rows.")
    
    print("✅ Data loading complete!")

except sqlite3.IntegrityError as e:
    print(f"Integrity Error (Duplicate Data?): {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()
