import psycopg2
import csv

DB_USER = "postgres"
DB_PASSWORD = "aisana111"
DB_HOST = "localhost"
DB_NAME = "phonebook_db"

# 1. Подключение к существующей базе 

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    phone VARCHAR(20) NOT NULL UNIQUE
)
""")
conn.commit()

print("Table ready.")

# 3. Функции и процедуры PostgreSQL 

# Функция поиска по паттерну
cur.execute("""
CREATE OR REPLACE FUNCTION search_phonebook(p TEXT)
RETURNS TABLE (
    user_id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT *
    FROM phonebook pb
    WHERE pb.first_name ILIKE '%' || p || '%'
       OR pb.last_name  ILIKE '%' || p || '%'
       OR pb.phone      ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;
""")

# Процедура add_or_update_user
cur.execute("""
DROP PROCEDURE IF EXISTS add_or_update_user(VARCHAR, VARCHAR, VARCHAR);

CREATE OR REPLACE PROCEDURE add_or_update_user(
    fname VARCHAR,
    lname VARCHAR,
    ph VARCHAR
)
AS $$
BEGIN
    UPDATE phonebook
    SET first_name = fname,
        last_name = lname
    WHERE phone = ph;

    IF NOT FOUND THEN
        INSERT INTO phonebook(first_name, last_name, phone)
        VALUES (fname, lname, ph);
    END IF;
END;
$$ LANGUAGE plpgsql;
""")

# Процедура массовой вставки
cur.execute("""
DROP PROCEDURE IF EXISTS insert_many_users(TEXT[], TEXT[], TEXT[], TEXT[]);

CREATE OR REPLACE PROCEDURE insert_many_users(
    fnames TEXT[],
    lnames TEXT[],
    phones TEXT[],
    OUT invalid_data TEXT[]
)
AS $$
DECLARE
    i INT;
    bad_list TEXT[] := '{}';
BEGIN
    FOR i IN 1..array_length(fnames, 1) LOOP
        
        -- Номер только из цифр?
        IF phones[i] !~ '^[0-9]+$' THEN
            bad_list := array_append(bad_list,
                        fnames[i] || ' ' || lnames[i] || ' - invalid phone: ' || phones[i]);
            CONTINUE;
        END IF;

        -- Вставка/обновление
        INSERT INTO phonebook(first_name, last_name, phone)
        VALUES (fnames[i], lnames[i], phones[i])
        ON CONFLICT (phone) DO UPDATE
        SET first_name = EXCLUDED.first_name,
            last_name  = EXCLUDED.last_name;

    END LOOP;

    invalid_data := bad_list;
END;
$$ LANGUAGE plpgsql;
""")

# Пагинация
cur.execute("""
CREATE OR REPLACE FUNCTION get_phonebook_page(
    lim INT,
    off INT
)
RETURNS TABLE (
    user_id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT *
    FROM phonebook
    ORDER BY user_id
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;
""")

# Удаление
cur.execute("""
CREATE OR REPLACE PROCEDURE delete_user(val TEXT)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = val
       OR last_name  = val
       OR phone      = val;
END;
$$ LANGUAGE plpgsql;
""")

conn.commit()
print("All functions & procedures created.")



def insert_from_csv(path):
    names = []
    lnames = []
    phones = []

    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            names.append(r['first_name'])
            lnames.append(r['last_name'])
            phones.append(r['phone'])

    cur.execute("CALL insert_many_users(%s, %s, %s, NULL)", (names, lnames, phones))
    conn.commit()
    print("CSV inserted.")


def console_insert_one():
    fname = input("First name: ")
    lname = input("Last name: ")
    phone = input("Phone: ")

    cur.execute("CALL add_or_update_user(%s, %s, %s)", (fname, lname, phone))
    conn.commit()
    print("Inserted/updated.")


# Вариант A — вставка нескольких пользователей вручную
def console_insert_many():
    count = int(input("How many users to insert? "))

    fnames = []
    lnames = []
    phones = []

    for i in range(count):
        print(f"\nUser #{i+1}:")
        fnames.append(input("First name: "))
        lnames.append(input("Last name: "))
        phones.append(input("Phone: "))

    cur.execute("CALL insert_many_users(%s, %s, %s, NULL)", (fnames, lnames, phones))
    conn.commit()
    print("All users processed.")


def search_records():
    p = input("Enter pattern: ")

    cur.execute("SELECT * FROM search_phonebook(%s)", (p,))
    rows = cur.fetchall()

    if rows:
        for r in rows:
            print(r)
    else:
        print("Not found.")


def pagination():
    lim = int(input("Limit: "))
    off = int(input("Offset: "))

    cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (lim, off))
    rows = cur.fetchall()

    for r in rows:
        print(r)


def delete_entry():
    val = input("Enter name/phone to delete: ")
    cur.execute("CALL delete_user(%s)", (val,))
    conn.commit()
    print("Deleted.")

#  5. МЕНЮ 

while True:
    print("\nMENU:")
    print("1) Insert from CSV")
    print("2) Insert ONE user (console)")
    print("3) Insert MANY users ")
    print("4) Search (pattern)")
    print("5) Pagination")
    print("6) Delete")
    print("7) Exit")

    choice = input("Choose option: ")

    if choice == "1":
        insert_from_csv("phonebook.csv")
    elif choice == "2":
        console_insert_one()
    elif choice == "3":
        console_insert_many()   
    elif choice == "4":
        search_records()
    elif choice == "5":
        pagination()
    elif choice == "6":
        delete_entry()
    elif choice == "7":
        break
    else:
        print("Invalid option.")

cur.close()
conn.close()
