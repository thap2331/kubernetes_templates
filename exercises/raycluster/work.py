import ray
import time

# --- 1. Define a remote function (a task Ray can execute) ---
@ray.remote
def multiply_and_sleep(x, y, sleep_time=1):
    """
    Multiplies two numbers and sleeps for a specified duration.
    """
    print(f"Task starting for {x} * {y}")
    time.sleep(sleep_time)
    result = x * y
    print(f"Task finished, result: {result}")
    return result

# --- 2. Initialize Ray (connect to the cluster) ---
def main():
    # If running inside the k3d cluster as a pod, Ray might auto-detect the cluster.
    # If running locally, you must specify the address of the Ray head service.
    # Replace 'ray-head-service.ray-namespace.svc.cluster.local:10001' with your service endpoint.
    try:
        # Example for connecting to a specific remote cluster address:
        # ray.init(address="ray://<YOUR_CLUSTER_HEAD_IP/HOSTNAME>:10001")
        
        # Example for connecting locally (if this script runs on the head node or auto-detect is working in k8s):
        ray.init(address="auto")
        print("Successfully connected to the Ray cluster.")
    except ConnectionError as e:
        print(f"Failed to connect to Ray cluster: {e}")
        print("Please ensure your Ray cluster is running and the address is correct.")
        return

    # --- 3. Run remote tasks asynchronously ---
    print("\nDispatching tasks...")
    # Call the remote function using .remote() instead of ()
    future_results = []
    for i in range(5):
        # Each .remote() call immediately returns a future (ObjectRef)
        ref = multiply_and_sleep.remote(i, 10, sleep_time=2)
        future_results.append(ref)
    
    # --- 4. Wait for results and retrieve them ---
    print(f"Tasks dispatched. Waiting for {len(future_results)} results...")
    # ray.get() blocks until the results are available from the cluster workers
    results = ray.get(future_results)
    
    print("\nAll results received:")
    print(results) # e.g., [0, 10, 20, 30, 40]
    
    # --- 5. Shut down the connection ---
    ray.shutdown()

if __name__ == "__main__":
    main()
