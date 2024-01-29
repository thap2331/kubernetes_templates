# Exercise 5-05 - Serverless

## Prompt - Serverless

## Prereqs

## Hint
- I did not finish this.
- Get started: Copy directory ex-5-02-service-mesh as ex-5-05-serverless
- cd to this directory
- Follow this [tutorial](https://devopswithkubernetes.com/part-5/4-beyond-kubernetes)
- Build and push the docker images
- Delete kustomization (if you do not want to use it)
- Update start cluster
    - Add `--k3s-arg "--disable=traefik@server:0"` while starting a cluster
- Get ksvc `kubectl get ksvc -n logtest`
- `curl -H "Host: http://nativeservice.todotest.svc.cluster.local" http://localhost:8081`


## Test

## Solution
- cd to this directory, run `make relaunch-cluster`
- I did not finish this

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-5/4-beyond-kubernetes)</i>