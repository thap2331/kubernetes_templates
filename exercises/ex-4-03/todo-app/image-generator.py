import requests, schedule, time, datetime, os

image_url = "https://picsum.photos/1200"
image_filename = f"{datetime.date.today().strftime('%Y-%m-%d')}.jpg"
persistent_vol_path = '/usr/src/app/files'

def fetch_new_image():

    global image_url, image_filename
    """Requests a new URL and saves it to a file.
    Args:
        url: The URL to request.
        filename: The filename to save the content to.
    """
    with open(f'{persistent_vol_path}/{image_filename}', "wb") as f:
        print("Fetching new image...")
        f.write(requests.get(image_url).content)

#Prod: Schedule the fetch_new_image function to run every day at midnight
# schedule.every().day.at("00:00").do(fetch_new_image)

#Test: Schedule the fetch_new_image function to run every 10 seconds
schedule.every(10).seconds.do(fetch_new_image)

def check_file_exists_for_today():
    path = f'{persistent_vol_path}/{image_filename}'
    if os.path.exists(path):
        print('File exists')
    else:
        print('File does not exist. Get a new image.')
        fetch_new_image()

check_file_exists_for_today()

# Run the scheduled tasks in a separate thread
def run_scheduled_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)

run_scheduled_tasks()