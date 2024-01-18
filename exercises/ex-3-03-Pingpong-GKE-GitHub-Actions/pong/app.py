import random, string, logging, psycopg2, os
from flask import Flask, render_template
from psycopg2.extras import RealDictCursor

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#Connect to local postgres pod
def connect_to_postgres():
    conn = psycopg2.connect(
        host="postgres-svc",
        database=os.getenv('POSTGRES_DB'), 
        user=os.getenv('POSTGRES_USER'), 
        password=os.getenv('POSTGRES_PASSWORD')
        )
    return conn

app = Flask(__name__)

def get_first_row():
    postgres_conn = connect_to_postgres()
    postgres_cursor = postgres_conn.cursor(cursor_factory=RealDictCursor)
    postgres_cursor.execute("SELECT * FROM pongtable WHERE id = 1")
    row = postgres_cursor.fetchone()
    postgres_cursor.close()
    postgres_conn.close()
    
    return row

def insert_into_db(count, ingestion_type=None):
    postgres_conn = connect_to_postgres()
    postgres_cursor = postgres_conn.cursor()
    if ingestion_type == 'update':
        postgres_cursor.execute("UPDATE pongtable SET count = %s WHERE id = 1", (count,))
        postgres_conn.commit()
    elif ingestion_type == 'insert':
        postgres_cursor.execute("INSERT INTO pongtable (count) VALUES (%s)", [count])
        postgres_conn.commit()
    else:
        logging.error('Incorrect ingestion type specified')
    postgres_cursor.close()
    postgres_conn.close()

    return


def ingest_to_postgres(count):
    postgres_conn = connect_to_postgres()
    postgres_cursor = postgres_conn.cursor()
    # Add row if not exists, else update row
    postgres_cursor.execute("SELECT * FROM pongtable WHERE id = 1")
    row = postgres_cursor.fetchone()
    if row is None:
        postgres_cursor.execute("INSERT INTO pongtable (count) VALUES (%s)", [count])
    else:
        postgres_cursor.execute("UPDATE pongtable SET count = %s WHERE id = 1", (count,))
    postgres_conn.commit()
    postgres_cursor.close()
    postgres_conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pingpong')
def pong():
    row = get_first_row()
    if row:
        counter=row['count']
        counter+=1
        insert_into_db(counter, 'update')
    else:
        counter=1
        insert_into_db(counter, 'insert')
    msg=f'Pong: {counter}\n'

    return render_template('show.html', message=msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)