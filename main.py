import psycopg2
from contextlib import contextmanager

@contextmanager
def postgresql_connection(dbname, user, password, host, port):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print(f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()

# usage
with postgresql_connection(dbname="your_database_name", user="your_username", password="your_password", host="your_host", port="your_port") as cursor:
    query = "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)"
    values = ("value1", "value2", "value3")
    cursor.execute(query, values)
