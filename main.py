import psycopg2
from contextlib import contextmanager

@contextmanager
def postgresql_connection(dbname, user, password, host, port):
    """
    Creates a context manager for a PostgreSQL database connection.

    Args:
        dbname (str): The name of the database to connect to.
        user (str): The username for the database connection.
        password (str): The password for the database connection.
        host (str): The host address of the database server.
        port (str): The port number for the database server.

    Yields:
        psycopg2.extensions.cursor: A cursor object for executing SQL statements.
    """
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
