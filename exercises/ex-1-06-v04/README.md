
## Prompt: Use a NodePort Service to enable access to the project.
    - [DevOps with Kubernetes](https://devopswithkubernetes.com/part-1/3-introduction-to-networking)
## Get started: Copy directory ex-1-02-v02 as ex-1-06-v04.
## Hint
- 1
    ```
        Create a file service.yaml into the manifests folder and we need the service to do the following things:

        Declare that we want a Service
        Declare which port to listen to
        Declare the application where the request should be directed to
        Declare the port where the request should be directed to
    ```

## Test: http://localhost:8082/ should work.
## Notes:
    - If you are using a flask app, do not forget to expose the port from the app.

## Solution
    - cd to this directory, run `make relaunch-cluster` and check http://localhost:8082/.