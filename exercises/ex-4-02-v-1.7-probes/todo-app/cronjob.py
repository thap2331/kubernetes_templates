import psycopg2, os, random
from psycopg2.extras import RealDictCursor

#Connect to local postgres pod
def connect_to_postgres():
    conn = psycopg2.connect(
        host="postgres-svc",
        database=os.getenv('POSTGRES_DB'), 
        user=os.getenv('POSTGRES_USER'), 
        password=os.getenv('POSTGRES_PASSWORD')
        )
    return conn

def upsert_delete(data, ingest_type='insert'):
    postgres_conn = connect_to_postgres()
    postgres_cursor = postgres_conn.cursor()
    title = data.get('title')
    description = data.get('description')
    id = data.get('id')
    if ingest_type=='insert':
        postgres_cursor.execute("INSERT INTO todotable (title, description) VALUES (%s, %s)", [title, description])
    elif ingest_type=='update':
        postgres_cursor.execute("UPDATE todotable SET title = (%s), description = (%s) WHERE id = (%s)", (title, description, id))
    elif ingest_type=='delete':
        postgres_cursor.execute("DELETE FROM todotable WHERE id = (%s)", (id,))
    postgres_conn.commit()
    postgres_cursor.close()
    postgres_conn.close()

def get_all_data():
    postgres_conn = connect_to_postgres()
    postgres_cursor = postgres_conn.cursor(cursor_factory=RealDictCursor)
    postgres_cursor.execute("SELECT * FROM todotable")
    data = postgres_cursor.fetchall()
    postgres_cursor.close()
    postgres_conn.close()
    data = [dict(i) for i in data]
    return data

if __name__ == "__main__":
    title = f"random-{random.randint(0, 999999999999)}"
    description = 'Enter description: '
    tasks = get_all_data()
    new_task = {'id': len(tasks) + 1, 'title': title, 'description': description}
    upsert_delete(data=new_task, ingest_type='insert')
