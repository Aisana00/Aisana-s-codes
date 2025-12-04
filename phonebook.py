import psycopg2
import csv


DB_USER = "postgres"
DB_PASSWORD = "aisana111"
DB_HOST = "localhost"
DB_NAME = "phonebook_db"


conn = psycopg2.connect(
    host=DB_HOST,
    database="postgres",
    user=DB_USER,
    password=DB_PASSWORD
)
conn.autocommit = True
cur = conn.cursor()

cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (DB_NAME,))
exists = cur.fetchone()
if not exists:
    cur.execute(f"CREATE DATABASE {DB_NAME};")
    print(f"Database '{DB_NAME}' created")
else:
    print(f"The database '{DB_NAME}' already exists")

cur.close()
conn.close()

# Подключаемся к phonebook_db 
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cur = conn.cursor()

#  Создание таблицы 
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    phone VARCHAR(20) NOT NULL UNIQUE
)
""")
conn.commit()
print("Table 'phonebook' is ready.")

#  Вставка данных из CSV
def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
                (row['first_name'], row['last_name'], row['phone'])
            )
    conn.commit()
    print("Date from CSV is displayed.")

#  Ввод с консоли 
def insert_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    cur.execute(
        "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
        (first_name, last_name, phone)
    )
    conn.commit()
    print("The date is posted")

#  UPDATE 
def update_contact():
    phone = input("Enter the number you want to change: ")
    new_phone = input("Enter the new number: ")

    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE phone=%s",
        (new_phone, phone)
    )
    conn.commit()
    print("Number has been updated.")

#  SEARCH
def search():
    text = input(" Enter the name and number to search: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE first_name=%s OR phone=%s",
        (text, text)
    )
    rows = cur.fetchall()

    if rows:
        for r in rows:
            print(r)
    else:
        print("Nothing found.")

# DELETE 
def delete_contact():
    text = input("Enter a name or number to delete: ")

    cur.execute(
        "DELETE FROM phonebook WHERE first_name=%s OR phone=%s",
        (text, text)
    )
    conn.commit()
    print("Contact deleted")


while True:
    print("\nMenu:")
    print("1) CSV Insert")
    print("2) Console Insert")
    print("3) Update contact")
    print("4) Search")
    print("5) Delete")
    print("6) Exit")

    choice = input("Choose: ")

    if choice == "1":
        insert_from_csv("phonebook.csv")
    elif choice == "2":
        insert_from_console()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        search()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice")


cur.close()
conn.close()
