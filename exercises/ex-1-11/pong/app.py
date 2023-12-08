import random, string, datetime, time, logging
from flask import Flask, render_template, request, redirect, url_for

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



app = Flask(__name__)

counter = 0

@app.route('/pingpong')
def pong():
    global counter
    counter+=1
    msg=f'Pong: {counter}\n'

    storage_mount_path = '/usr/src/app/files'
    with open(f'{storage_mount_path}/log.txt', 'a') as f:
        f.write(msg)

    return render_template('show.html', message=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
