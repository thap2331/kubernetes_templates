# Exercise 4-01: Update Strategies and Prometheus
## Prompt: Add Readiness Probe

## Hint
- Copy directory ex-2-07 as ex-4-01-Readiness-Probes
- Update pong app to allow for checking if the app is ready
- Update log output app to allow for checking if the app is ready
- If you are switching back from using cloud to local cluster, do `docker system prune -af`

## Tests
    - This http://localhost:8081/pingpong should show your `MESSAGE` environment variable.

## Notes:

## Solution
    - cd to this directory, run `make relaunch-cluster`. It should show your `MESSAGE` environment variable as configured in the app.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-2/4-statefulsets-and-jobs)</i>