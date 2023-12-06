# Exercise 1.09: More services
## Prompt: More services with Log Output Application
    - Develop a second application that simply responds with "pong 0" to a GET request and increases a counter (the 0) so that you can see how many requests have been sent. The counter should be in memory so it may reset at some point. Create a new deployment for it and have it share ingress with "Log output" application. Route requests directed '/pingpong' to it.

    - Important: The ping-pong application will need to listen requests on '/pingpong', so you may have to make changes to its code.

## Get started: Copy directory ex-1-09 as ex-1-11.
## Hint
- Helpful commands
    - `kubectl get pv example-pv`
    - `kubectl get pvc file-claim`
- Create second app as requested.
    - Add an app.
    - Create a dockerfile for it.
- In manifests:
    - Add `pong-deployment.yaml`
    - Add `pong-service.yaml`
- Update the ingress:
    - Add a new `path`

## Make sure both tests work
    - If http://localhost:8081/now works, then we know it works. Every time you refresh should give you new timestamp and string.
    - If http://localhost:8081/pingpong works, then we know it works.

## Notes:
    - Remember, you need to make change in the code to make sure the ingress path works properly. I spent stupid amount of time because I did not understand the directions.

## Solution
    - cd to this directory, run `make relaunch-cluster` and check http://localhost:8081/now and http://localhost:8081/pingpong .

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-1/3-introduction-to-networking)</i>