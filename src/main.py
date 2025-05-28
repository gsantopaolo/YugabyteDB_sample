from sql_client import SQLClient
from no_sql_client import NoSQLClient

def main():
    # SQL demo
    sql = SQLClient()
    sql.create_table()
    sql.insert_customer('Alice', 'alice@example.com', 30)
    sql.insert_customer('Bob', 'bob@example.com', 25)
    print("Customers:", sql.get_customers())
    sql.close()

    # NoSQL demo
    nosql = NoSQLClient()
    sample = {'name': 'Widget', 'price': 19.99, 'tags': ['tools', 'sale']}
    uid = nosql.insert_entity(sample)
    print("Fetched entity:", nosql.get_entity(uid))
    nosql.close()

if __name__ == '__main__':
    main()
