import psycopg2


conn = psycopg2.connect(
    host="localhost",      
    database="suppliers",  
    user="postgres",       
    password="aisana111" 
)

# Создание курсора 
cur = conn.cursor()

# Проверка подключения
cur.execute("SELECT version();")
db_version = cur.fetchone()
print(f"Connected to PostgreSQL database. Version: {db_version}")


cur.close()
conn.close()
