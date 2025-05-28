import os
import json
from uuid import uuid4
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

class NoSQLClient:
    def __init__(self):
        host = os.getenv('YB_HOST', 'localhost')
        port = int(os.getenv('YB_CQL_PORT', 9042))
        auth_provider = PlainTextAuthProvider(
            username=os.getenv('YB_USER', 'yugabyte'),
            password=os.getenv('YB_PASSWORD', 'yugabyte')
        )
        self.cluster = Cluster([host], port=port, auth_provider=auth_provider)
        self.session = self.cluster.connect()
        # Create keyspace if not exists
        self.session.execute("""
            CREATE KEYSPACE IF NOT EXISTS demo
            WITH replication = {'class':'SimpleStrategy', 'replication_factor':1};
        """)
        self.session.set_keyspace('demo')
        # Create table to store JSON data
        self.session.execute("""
            CREATE TABLE IF NOT EXISTS entities (
                id UUID PRIMARY KEY,
                data text
            );
        """)

    def insert_entity(self, payload: dict):
        uid = uuid4()
        self.session.execute(
            "INSERT INTO entities (id, data) VALUES (%s, %s);",
            (uid, json.dumps(payload))
        )
        return uid

    def get_entity(self, uid):
        row = self.session.execute(
            "SELECT data FROM entities WHERE id=%s;", (uid,)
        ).one()
        return json.loads(row.data) if row else None

    def close(self):
        self.cluster.shutdown()
