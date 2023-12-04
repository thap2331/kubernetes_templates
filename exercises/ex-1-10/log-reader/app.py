import random, string, datetime, time, logging, os
from flask import Flask, render_template, request, redirect, url_for

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

storage_mount_path = '/usr/src/app/files'

app = Flask(__name__)

# Index route to display all tasks
@app.route('/')
def index():
    return render_template('index.html')

# Route to display the form for adding a new task
@app.route('/show')
def new():
    with open(f'{storage_mount_path}/log.txt', 'r') as f:
        for line in f:
            pass
        last_line = line
    return render_template('show.html', message=last_line)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
