import psycopg2


DB_USER = "postgres"        
DB_PASSWORD = "aisana111"  
DB_HOST = "localhost"
DB_NAME = "suppliers"       

# Подключение к базе suppliers
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cur = conn.cursor()



# 1. Table vendors
cur.execute("""
CREATE TABLE IF NOT EXISTS vendors (
    vendor_id SERIAL PRIMARY KEY,
    vendor_name VARCHAR(255) NOT NULL,
    vendor_address VARCHAR(255)
)
""")

# 2. Table parts
cur.execute("""
CREATE TABLE IF NOT EXISTS parts (
    part_id SERIAL PRIMARY KEY,
    part_name VARCHAR(255) NOT NULL,
    part_price NUMERIC
)
""")

# 3. Table parts_drawings
cur.execute("""
CREATE TABLE IF NOT EXISTS parts_drawings (
    part_id INT PRIMARY KEY,
    drawing BYTEA,
    FOREIGN KEY (part_id) REFERENCES parts (part_id)
)
""")

# 4. Table vendor_parts
cur.execute("""
CREATE TABLE IF NOT EXISTS vendor_parts (
    vendor_id INT,
    part_id INT,
    PRIMARY KEY (vendor_id, part_id),
    FOREIGN KEY (vendor_id) REFERENCES vendors (vendor_id),
    FOREIGN KEY (part_id) REFERENCES parts (part_id)
)
""")


conn.commit()
print("All tables have been created.")


cur.close()
conn.close()
