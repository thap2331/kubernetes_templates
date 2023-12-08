from flask import Flask, render_template, request, redirect, url_for
import logging, datetime

persistent_vol_path = '/usr/src/app/files'
# persistent_vol_path = 'static'

app = Flask(__name__, static_folder=persistent_vol_path)

 
# In-memory data store (replace this with a database in a real application)
tasks = [
    {'id': 1, 'title': 'Task 1', 'description': 'Description for Task 1'},
    {'id': 2, 'title': 'Task 2', 'description': 'Description for Task 2'},
    {'id': 3, 'title': 'Task 3', 'description': 'Description for Task 3'},
]

# Index route to display all tasks
@app.route('/', methods=['GET', 'POST'])
def index():
    today = datetime.date.today().strftime("%Y-%m-%d")
    today_image_name = f'{today}.jpg'    
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template('index.html', user_input=user_input)
    else:
        return render_template('index.html', tasks=tasks, imagepath=today_image_name, user_input=None)

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
    if len(title) > 140:
        print('Title is too long')
        return redirect(url_for('index'))
    description = "task description" #request.form['description']
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
    app.run(host='0.0.0.0', port=5000, debug=True)
