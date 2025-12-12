import pandas as pd
import sqlite3
import os

# Configuration
DB_NAME = 'sales_analysis.db'
TABLE_NAME = 'sales_data'
CSV_FILE = r'C:\Users\ABHILASH\Desktop\hcl\FINAL_DATASET.csv' 

# --- 1. Load Data ---
if not os.path.exists(CSV_FILE):
    print(f"Error: CSV file '{CSV_FILE}' not found. Please add your data file.")
    exit()

df = pd.read_csv(CSV_FILE)
print(f"Loaded {len(df)} rows from CSV. Starting insertion...")

# --- 2. Connect and Insert ---
try:
    # Connects to the database file (creates it if it doesn't exist)
    conn = sqlite3.connect(DB_NAME)
    
    # Define SQL data types explicitly for precision (optional but recommended)
    dtype_map = {
        'date': 'TEXT',
        'order_id': 'INTEGER',
        'price': 'REAL',
        'promotion_flag': 'INTEGER',
        'total_sales': 'REAL',
        'branch_id': 'TEXT',
        # ... map other columns similarly using TEXT, INTEGER, REAL
    }
    
    # Write DataFrame to SQL table
    df.to_sql(
        TABLE_NAME, 
        conn, 
        if_exists='replace', # Replace table if it already exists
        index=False,         # Don't save the pandas index as a column
        dtype=dtype_map      # Use the explicit type mapping
    )
    
    print(f"✅ Data successfully inserted into table '{TABLE_NAME}' in '{DB_NAME}'.")

    # --- 3. Run a verification query ---
    verification_df = pd.read_sql(f"SELECT COUNT(*) AS RowCount, SUM(total_sales) AS TotalRevenue FROM {TABLE_NAME};", conn)
    print("\nVerification Check:")
    print(verification_df)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()