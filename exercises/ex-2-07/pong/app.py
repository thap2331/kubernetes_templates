import random, string, datetime, time, logging, psycopg2, os
from flask import Flask, render_template, request, redirect, url_for

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

counter = 0

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

@app.route('/pingpong')
def pong():
    global counter
    counter+=1
    msg=f'Pong: {counter}\n'
    ingest_to_postgres(counter)

    return render_template('show.html', message=msg)

@app.route('/count')
def get_pong_count():
    global counter
    pong_count = {'pong_count': counter}

    return pong_count


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)