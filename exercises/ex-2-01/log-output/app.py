import random, string, datetime, requests
from flask import Flask, render_template

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
    pong_refresh_count = requests.get('http://pingpong-svc:3001/count').json()
    # pong_refresh_count = requests.get('http://localhost:8081/count').json()
    pong_refresh_count = f"pong: {pong_refresh_count['pong_count']}"

    return render_template('show.html', message1=msg, message2=pong_refresh_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
