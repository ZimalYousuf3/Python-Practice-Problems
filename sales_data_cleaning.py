# TASK: load sales.csv, fill missing values, and print the total sales per region (hint: df.groupby("region")["sales"].sum())

import pandas as pd

print(df.isnull().sum()) # count missing values per column (CHAINING)
print()

# Strategy A: Drop rows with any missing value
df_dropped = df.dropna()

# Strategy B: Fill missing values with average
avg = df['sales'].mean()
df_filled = df.copy()

df_filled['sales'] = df_filled['sales'].fillna(avg)
df_filled['region'] = df_filled['region'].fillna('Unknown')
total_sales = df_filled.groupby('region')['sales'].sum() # grouping by region

print(df_filled)
print()
print(total_sales)

