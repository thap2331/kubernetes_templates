import random, string, datetime, os, psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, render_template

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


app = Flask(__name__)

#Connect to local postgres pod
def connect_to_postgres():
    conn = psycopg2.connect(
        host="postgres-svc",
        database=os.getenv('POSTGRES_DB'), 
        user=os.getenv('POSTGRES_USER'), 
        password=os.getenv('POSTGRES_PASSWORD')
        )
    return conn

# Index route to display all tasks
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logready')
def log_ready():
    # Get count from postgres pod
    postgres_conn = connect_to_postgres()
    postgres_cursor = postgres_conn.cursor(cursor_factory=RealDictCursor)
    postgres_cursor.execute("SELECT * FROM pongtable WHERE id = 1")
    row = postgres_cursor.fetchone()
    if row:
        return render_template('index.html'), 200
    else:
        return render_template('index.html'), 500


# Route to display the form for adding a new task
@app.route('/now')
def new():
    msg=f'Time: {datetime.datetime.now()},\t\t Random id: {id_generator()}'
    # Get count from postgres pod
    postgres_conn = connect_to_postgres()
    postgres_cursor = postgres_conn.cursor(cursor_factory=RealDictCursor)
    postgres_cursor.execute("SELECT * FROM pongtable WHERE id = 1")
    row = postgres_cursor.fetchone()
    pong_refresh_count = f"pong: {row['count']}"
    postgres_cursor.close()
    postgres_conn.close()

    return render_template('show.html', message1=msg, message2=pong_refresh_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)