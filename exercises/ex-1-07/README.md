## Prompt: External access with Ingress
    -  "Log output" application currently outputs a timestamp and a random string to the logs.
    - Add an endpoint to request the current status (timestamp and string) and an ingress so that you can access it with a browser.

You can just store the string and timestamp to the memory.
## Get started: Copy directory ex-1-03 as ex-1-07.
## Hint
- Create an access to loadbalancer while creating the cluster.
    - We will have access through port 8081 to our server node (actually all nodes).
- Update the app to make it a flask app.
    - Add app folder.
        - Add templates.
        - Update `app.py` to flask app. Add a new endpoint for current status (timestamp and string).
    - Add `ingress` and `service` to manifests folder.

## Test
    - If http://localhost:8081/show works, then we know it works. Every time you refresh should give you new timestamp and string.

## Notes:
    - I do not understand the difference between, Exercise 1.07: External access with Ingress and Exercise 1.08: Project v0.5. Please let me know how are they different.
    - If you are using a flask app, do not forget to expose the port from the app.

## Solution
    - cd to this directory, run `make relaunch-cluster` and check http://localhost:8081/show.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-1/3-introduction-to-networking)</i>