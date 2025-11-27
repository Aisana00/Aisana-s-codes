import psycopg2

DB_USER = "postgres"
DB_PASSWORD = "aisana111"
DB_HOST = "localhost"

 
conn = psycopg2.connect(
    host=DB_HOST,
    database="postgres",
    user=DB_USER,
    password=DB_PASSWORD
)
conn.autocommit = True
cur = conn.cursor()

# Проверяем, существует ли база suppliers
cur.execute("SELECT 1 FROM pg_database WHERE datname='suppliers';")
exists = cur.fetchone()

if not exists:
    cur.execute("CREATE DATABASE suppliers;")
    print("Base 'suppliers' created.")
else:
    print("Base 'suppliers' already exists.")

cur.close()
conn.close()
