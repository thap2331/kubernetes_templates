import ray
import time

# Initialize Ray.
ray.init()

@ray.remote
def square(x):
    return x * x

# Create a few tasks.
futures = [square.remote(i) for i in range(4)]

# Initialize the sleep time
sleep_time = 10  # Start with 10 seconds

# Loop 5 times, doubling the sleep time each time
for _ in range(5):
    # Wait for the tasks to complete and collect the results.
    results = ray.get(futures)

    # Print the results.
    print('results:',results)

    # Sleep for the current sleep time
    time.sleep(sleep_time)

    # Double the sleep time
    sleep_time *= 2

# Shutdown Ray.
ray.shutdown()