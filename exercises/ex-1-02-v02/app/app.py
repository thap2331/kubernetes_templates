import logging
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store (replace this with a database in a real application)
tasks = [
    {'id': 1, 'title': 'Task 1', 'description': 'Description for Task 1'},
    {'id': 2, 'title': 'Task 2', 'description': 'Description for Task 2'},
    {'id': 3, 'title': 'Task 3', 'description': 'Description for Task 3'},
]

# Index route to display all tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to display the form for adding a new task
@app.route('/new')
def new():
    return render_template('new.html')

# Route to handle the creation of a new task
@app.route('/create', methods=['POST'])
def create():
    title = request.form['title']
    description = request.form['description']
    
    new_task = {'id': len(tasks) + 1, 'title': title, 'description': description}
    tasks.append(new_task)

    return redirect(url_for('index'))

# Route to display the details of a task
@app.route('/<int:task_id>')
def show(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    return render_template('show.html', task=task)

# Route to display the form for editing a task
@app.route('/<int:task_id>/edit')
def edit(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    return render_template('edit.html', task=task)

# Route to handle the update of a task
@app.route('/<int:task_id>/update', methods=['POST'])
def update(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    task['title'] = request.form['title']
    task['description'] = request.form['description']

    return redirect(url_for('index'))

# Route to handle the deletion of a task
@app.route('/<int:task_id>/delete')
def delete(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Server started in port 5001 test')
    app.run(debug=True)
