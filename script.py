import pandas as pd
from sqlalchemy import create_engine
import os

# Ruta del archivo Excel
ruta = "/Users/arturoesteva/Documents/python/carros_v2-2.xlsx"

if not os.path.exists(ruta):
    print("No se encontró el archivo, revisa la ruta.")
    exit()

# Leer datos del Excel
df = pd.read_excel(ruta)

# Generar tabla de tipos
column_types = []
for column in df.columns:
    dtype = df[column].dtype

    if pd.api.types.is_integer_dtype(dtype):
        tipo_analitico = "Cuantitativo discreto"
    elif pd.api.types.is_float_dtype(dtype):
        tipo_analitico = "Cuantitativo continuo"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        tipo_analitico = "Fecha"
    else:
        tipo_analitico = "Cualitativo nominal"

    column_types.append({
        "Variable": column,
        "Tipo técnico": str(dtype),
        "Tipo analítico": tipo_analitico
    })

tabla_tipos = pd.DataFrame(column_types)

# Conexión a MySQL en Docker (mysql-carros en puerto 3307)
engine_url = "mysql+pymysql://root:StrongPass123@localhost:3307/carros_db"
engine = create_engine(engine_url)

# Subir tablas
df.to_sql(name="carros_v2", con=engine, if_exists="replace", index=False)
tabla_tipos.to_sql(name="tipos_carros_v2", con=engine, if_exists="replace", index=False)

print("✅ Tablas 'carros_v2' y 'tipos_carros_v2' creadas en MySQL.")
