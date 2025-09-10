
import pandas as pd
import pyodbc

#=======================#
# Настройки подключения #
#=======================#
conn_str = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=IP\\SQLEXPRESS,Port;"  # IP или имя сервера
    "Database=LG;"
    "UID=;" #User name
    "PWD=;" #password
    "Encrypt=no;"
    "TrustServerCertificate=no;"
)

# ====================#
# Extract + Transform #
# ====================#
df = pd.read_csv("/opt/airflow/data/transform.csv")


df = df[["title", "link", "published"]]
df['published'] = pd.to_datetime(df['published'], errors='coerce').dt.date


# ============#
# Load в базу #
# ============#

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

insert_sql = """
INSERT INTO dbo.articles (title, link, published)
VALUES (?, ?, ?)
"""

data = df.values.tolist()
cursor.executemany(insert_sql, data)

conn.commit()
cursor.close()
conn.close()

