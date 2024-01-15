# Exercise 2.06: Documentation and ConfigMaps
## Prompt: Connect with GKE

## Get started: 
- Install [gke](https://cloud.google.com/sdk/docs/install)
    - Initialize using `gcloud init`
- Copy directory ex-2-07 as ex-3-01-Pingpong-GKE

## Hint
- See the services
    - `kubectl get svc -n logtest`
- Update app to retrieve `MESSAGE` variable from environment.
- Add `envFrom` in spec of a container in your deployment.
- (This is the way I did it): Create a `.env` file.
- Add `kubectl` command to create a configmap after creating a cluster: `kubectl create configmap newconfig --from-env-file=.env --namespace=logtest`
## Tests
    - This http://localhost:8081/pingpong should show your `MESSAGE` environment variable.

## Notes:

## Solution
    - cd to this directory, run `make relaunch-cluster`. It should show your `MESSAGE` environment variable as configured in the app.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-3/1-introduction-to-gke)</i>