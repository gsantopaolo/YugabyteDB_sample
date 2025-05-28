# YugabyteDB Docker + Python Demo 🚀

Welcome to the **YugabyteDB Docker + Python Demo**! This project demonstrates how to spin up a local 
YugabyteDB cluster using Docker Compose and build a simple Python application that exercises both 
the PostgreSQL-compatible (YSQL) and Cassandra-compatible (YCQL) APIs. 😎

---

## 📝 Table of Contents

1. [Prerequisites](#-prerequisites)
2. [Docker Compose Setup](#-docker-compose-setup)
3. [Project Structure](#-project-structure)
4. [SQL Client (YSQL)](#-sql-client-ysql)
5. [NoSQL Client (YCQL)](#-nosql-client-ycql)
6. [Running the Application](#-running-the-application)
7. [Next Steps & Extensions](#-next-steps--extensions)

---

## 🔧 Prerequisites

Before you begin, make sure you have the following installed on your machine:

* 🐳 **Docker & Docker Compose**
* 🐍 **Conda**

* Create your env:
```bash
  conda create --name yougabyte python=3.11.7 
  ```

* Activate your env:

  ```bash
    conda activate yougabyte  
  ```

* Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```
---

## 🐳 Docker Compose Setup

1. Launch the cluster:

   ```bash
   cd deployment
   docker-compose up -d
   ```

2. Verify YSQL connectivity:

   ```bash
   docker exec -it yugabyte bash -c \
     '/home/yugabyte/bin/ysqlsh --echo-queries --host $(hostname)'
   ```

3. Verify YCQL connectivity:

   ```bash
   docker exec -it yugabyte bash -c \
     '/home/yugabyte/bin/cqlsh $(hostname) 9042'
   ```

---

## 📂 Project Structure

```plaintext

└── deployment
    ├── docker-compose.yml
└── src
    ├── sql_client.py
    ├── nosql_client.py
    └── main.py
```

* **`deployment/docker-compose.yml`**: Defines the local YugabyteDB single-node cluster.
* **`src/sql_client.py`**: PostgreSQL (YSQL) client using `psycopg2-binary`.
* **`src/nosql_client.py`**: Cassandra (YCQL) client using `cassandra-driver`.
* **`src/main.py`**: Ties both clients together in a demo script.

---

## 🐘 SQL Client (YSQL)

Located in `app/sql_client.py`, this class:

* Connects to YSQL on port **5433**
* Creates a `customers` table
* Inserts and reads customer records

Key methods:

* `create_table()`: Creates `customers` if not exists ✅
* `insert_customer(name, email, age)`: Adds a new customer ✍️
* `get_customers()`: Fetches all customer rows 📋

---

## ☕ NoSQL Client (YCQL)

Located in `app/nosql_client.py`, this class:

* Connects to YCQL on port **9042**
* Creates a `demo` keyspace and `entities` table
* Inserts and reads JSON payloads stored as text

Key methods:

* `insert_entity(payload: dict)`: Stores a JSON object and returns its UUID 📦
* `get_entity(uid)`: Retrieves and parses the JSON by UUID 🔍

---

## ▶️ Running the Application

1. Navigate to the `app/` directory.
2. Run the demo script:

   ```bash
   python3 main.py
   ```

You should see output like:

```plaintext
Customers: [{'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'age': 30},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com', 'age': 25}]
Fetched entity: {'name': 'Widget', 'price': 19.99, 'tags': ['tools', 'sale']}
```

---

## 🌟 Next Steps & Extensions

* Add error handling and logging 🛡️
* Implement connection pooling for production use 🔄
* Scale to a multi-node YugabyteDB cluster 🌐
* Explore advanced YSQL and YCQL features (transactions, indexes, UDFs) ⚙️

Enjoy experimenting with YugabyteDB! If you have questions or suggestions, feel free to submit an issue or PR. 🚀
