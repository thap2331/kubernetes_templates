import random, string, datetime, time, logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

while True:
    msg=f'{datetime.datetime.now()},{id_generator()}'
    logging.info(msg)    
    time.sleep(5)