import datetime, time, logging, os

storage_mount_path = '/usr/src/app/files'
# os.makedirs(storage_mount_path)

logging.basicConfig(filename=f'{storage_mount_path}/log.txt', 
                    encoding='utf-8',
                    filemode='w',
                    level=logging.DEBUG)

while True:
    msg={"Time":{datetime.datetime.now()}}
    logging.info(msg)
    time.sleep(5)