from flask import Flask, render_template, request, redirect, url_for
import logging, datetime, psycopg2, os
from psycopg2.extras import RealDictCursor

persistent_vol_path = '/usr/src/app/files'

app = Flask(__name__, static_folder=persistent_vol_path)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

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
    done = data.get('done')
    id = data.get('id')
    if ingest_type=='insert':
        postgres_cursor.execute("INSERT INTO todotable (title, description) VALUES (%s, %s)", [title, description])
    elif ingest_type=='update':
        postgres_cursor.execute("UPDATE todotable SET title = (%s), description = (%s), done = (%s) WHERE id = (%s)", (title, description, done, id))
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

# Index route to display all tasks
@app.route('/', methods=['GET', 'POST'])
def index():
    today = datetime.date.today().strftime("%Y-%m-%d")
    today_image_name = f'{today}.jpg'    
    if request.method == 'POST':
        user_input = request.form['user_input']
        msg = f'Logging user input: {user_input} for post request'
        app.logger.info(msg)
        return render_template('index.html', user_input=user_input)
    else:
        tasks = get_all_data()
        msg = f'Logging for get request'
        app.logger.info(msg)
        return render_template('index.html', tasks=tasks, imagepath=today_image_name, user_input=None)

@app.route('/ready')
def ready():
    postgres_conn = connect_to_postgres()
    if postgres_conn:
        return render_template('index.html'), 200
    else:
        return render_template('index.html'), 500

@app.route('/test_obtain_input', methods=['POST'])
def route_test_obtain_input():
    text = request.form['text']
    print(text)
    ##you can do whatever you want with it after, here I just reinjecting it in my test page
    return render_template('index.html', message = text)

# Route to display the form for adding a new task
@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/unique')
def unique():
    return render_template('unique.html')

# Route to handle the creation of a new task
@app.route('/create', methods=['POST'])
def create():
    title = request.form['user_input']
    if len(title) > 10:
        msg='Title is longer than 10 characters'
        app.logger.info(msg)
        return redirect(url_for('index'))
    description = "task description" #request.form['description']
    tasks = get_all_data()
    new_task = {'id': len(tasks) + 1, 'title': title, 'description': description}
    msg = f'Logging new task: {new_task} in create route'
    app.logger.info(msg)
    upsert_delete(data=new_task, ingest_type='insert')

    return redirect(url_for('index'))

# Route to display the details of a task
@app.route('/<int:task_id>')
def show(task_id):
    tasks = get_all_data()
    task = next((task for task in tasks if task['id'] == task_id), None)
    app.logger.info(f'All tasks: {tasks}')
    return render_template('show.html', task=task)

@app.route('/todos/<int:task_id>', methods=['PUT'])
def update_to_done(task_id):
    tasks = get_all_data()
    app.logger.info(f'All tasks: {tasks}')
    task_to_be_updated = {}
    for i in tasks:
        app.logger.info(f"in loop id:{i['id']}, task id: {task_id}")
        app.logger.info(f"task in loop: {i}, check: {i['id'] == task_id}")
        if i['id'] == task_id:
            task_to_be_updated = i
            break
    app.logger.info(f'task to be updated: {task_to_be_updated}, task id:{task_id}')
    task_to_be_updated['done']='done'
    app.logger.info(f'after to be updated: {task_to_be_updated}, task id:{task_id}')
    upsert_delete(data=task_to_be_updated, ingest_type='update')
    return render_template('index.html')

# Route to display the form for editing a task
@app.route('/<int:task_id>/edit')
def edit(task_id):
    tasks = get_all_data()
    task = next((task for task in tasks if task['id'] == task_id), None)
    return render_template('edit.html', task=task)

# Route to handle the update of a task
@app.route('/<int:task_id>/update', methods=['POST'])
def update(task_id):
    task={}
    task['id'] = task_id
    task['title'] = request.form['title']
    task['description'] = request.form['description']
    task['done'] = request.form['done']
    upsert_delete(data=task, ingest_type='update')

    return redirect(url_for('index'))

# Route to handle the deletion of a task
@app.route('/<int:task_id>/delete')
def delete(task_id):
    upsert_delete(data={'id': task_id}, ingest_type='delete')

    return redirect(url_for('index'))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
    app.run(host='0.0.0.0', port=5000, debug=True)
