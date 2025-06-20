
### 2.1 `app/sql_client.py`

import os
import psycopg2
from psycopg2.extras import RealDictCursor

class SQLClient:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv('YB_HOST', 'localhost'),
            # host=os.getenv('YB_HOST', '127.0.0.1'),
            port=int(os.getenv('YB_YSQl_PORT', 5433)),
            user=os.getenv('YB_USER', 'yugabyte'),
            password=os.getenv('YB_PASSWORD', 'yugabyte'),
            dbname=os.getenv('YB_DB', 'yugabyte')
        )
        self.conn.autocommit = True

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS customers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            age INT
        );
        """
        with self.conn.cursor() as curs:
            curs.execute(sql)

    def insert_customer(self, name, email, age):
        sql = "INSERT INTO customers (name, email, age) VALUES (%s, %s, %s);"
        with self.conn.cursor() as curs:
            curs.execute(sql, (name, email, age))

    def get_customers(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as curs:
            curs.execute("SELECT * FROM customers;")
            return curs.fetchall()

    def close(self):
        self.conn.close()
