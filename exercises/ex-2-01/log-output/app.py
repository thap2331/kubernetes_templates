import random, string, datetime, time, logging
from flask import Flask, render_template, request, redirect, url_for

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


app = Flask(__name__)

# Index route to display all tasks
@app.route('/')
def index():
    return render_template('index.html')

# Route to display the form for adding a new task
@app.route('/now')
def new():
    msg=f'Time: {datetime.datetime.now()},\t\t Random id: {id_generator()}'
    pong_refresh_count = request('GET', 'http://pingpong-svc:3001/count')

    return render_template('show.html', message1=msg, message2=pong_refresh_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
