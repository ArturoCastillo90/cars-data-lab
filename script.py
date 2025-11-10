import pandas as pd
from sqlalchemy import create_engine
import os

# Path to the Excel file
path = "/Users/arturoesteva/Documents/python/carros_v2-2.xlsx"

if not os.path.exists(path):
    print("File not found, please check the path.")
    exit()

# Read Excel data
df = pd.read_excel(path)

# Generate a table with data types
column_types = []
for column in df.columns:
    dtype = df[column].dtype

    if pd.api.types.is_integer_dtype(dtype):
        analytic_type = "Quantitative discrete"
    elif pd.api.types.is_float_dtype(dtype):
        analytic_type = "Quantitative continuous"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        analytic_type = "Date"
    else:
        analytic_type = "Qualitative nominal"

    column_types.append({
        "Variable": column,
        "Technical Type": str(dtype),
        "Analytic Type": analytic_type
    })

# Convert to DataFrame
type_table = pd.DataFrame(column_types)

# MySQL connection (Docker container: mysql-carros on port 3307)
engine_url = "mysql+pymysql://root:StrongPass123@localhost:3307/carros_db"
engine = create_engine(engine_url)

# Upload both tables to MySQL
df.to_sql(name="carros_v2", con=engine, if_exists="replace", index=False)
type_table.to_sql(name="car_types_v2", con=engine, if_exists="replace", index=False)

print("✅ Tables 'carros_v2' and 'car_types_v2' successfully created in MySQL.")

