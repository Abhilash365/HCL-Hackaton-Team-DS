PRAGMA foreign_keys = ON;

-- 1. Product Lookup Table
CREATE TABLE IF NOT EXISTS Product_Lookup (
    product_id TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT
);

-- 2. Branch Lookup Table
CREATE TABLE IF NOT EXISTS Branch_Lookup (
    branch_id TEXT PRIMARY KEY,
    branch_name TEXT NOT NULL
);

-- 3. Sales Transactions (Correctly excludes names/categories)
CREATE TABLE IF NOT EXISTS Sales_Transactions (
    order_id INTEGER PRIMARY KEY,
    product_id TEXT NOT NULL,
    branch_id TEXT NOT NULL,
    date TEXT NOT NULL,
    day_of_week INTEGER,
    month INTEGER,
    price REAL,
    total_sales REAL NOT NULL,
    online_sales REAL,
    offline_sales REAL,
    returns_count REAL,
    promotion_flag INTEGER,
    festival_flag INTEGER,
    holiday_flag INTEGER,
    seasonal_index REAL,
    cpi REAL, 
    lag_1 REAL,
    lag_7 REAL,
    lag_30 REAL,
    rolling_mean_7 REAL,
    rolling_mean_30 REAL,
    FOREIGN KEY (product_id) REFERENCES Product_Lookup (product_id),
    FOREIGN KEY (branch_id) REFERENCES Branch_Lookup (branch_id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_sales_date ON Sales_Transactions (date);
CREATE INDEX IF NOT EXISTS idx_sales_product ON Sales_Transactions (product_id);
CREATE INDEX IF NOT EXISTS idx_sales_branch ON Sales_Transactions (branch_id);
