import random, string, datetime, time, logging
from flask import Flask, render_template, request, redirect, url_for

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


msg={"Time":{datetime.datetime.now()}}

while True:
    logging.info(msg)
    # overwrite message to a file if it exists else create a new file
    logging.basicConfig(filename='log.txt', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')


    time.sleep(5)

# app = Flask(__name__)

# Index route to display all tasks
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/show')
# def new():
#     msg=f'Time: {datetime.datetime.now()},\t\t Random id: {id_generator()}'
#     return render_template('show.html', message=msg)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
