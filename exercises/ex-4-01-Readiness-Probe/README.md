# Exercise 4-01: Update Strategies and Prometheus
## Prompt: Add Readiness Probe

## Hint
- Copy directory ex-2-07 as ex-4-01-Readiness-Probes
- Update pong app to allow for checking if the app is ready
- Update log output app to allow for checking if the app is ready
- We are saving docker images to a public dockerhub repo. In this way, our app can just pull a public image.
- Additional note: I am adding a root route, `/`, in the pong app.

## Tests

## Notes:

## Solution
- cd to this directory, run `make relaunch-cluster`. It should show your `MESSAGE` environment variable as configured in the app.
- See deployment apps. 
    - The logs of `LogPong` pod should show `"GET /pongready HTTP/1.1" 200 -`. The depolyment is going ok.
    - However, the `log-output` pod should show `"GET /logready HTTP/1.1" 500 -`. The deployment is not ready.
- See the ingress service, `kubectl get ing -n logtest`. Pick an address and go to `http://{{ ADDRESS }}/pingpong`.
    - Now the `log-output` pod should show `"GET /logready HTTP/1.1" 200 -`

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-4/1-update-strategies-and-prometheus)</i>