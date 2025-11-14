# Using Helm with k3d

## Prompt - Create readiness and liveness probes

## Prereqs
- Install [helm for ubuntu](https://helm.sh/docs/intro/install/#from-apt-debianubuntu)
- Follow this [article](https://medium.com/@munza/local-kubernetes-with-k3d-helm-dashboard-6510d906431b)

## Hint
- Get started: Copy directory ex-2-10-v-1.3-monitoring to ex-4-02-v-1.7-probes
- Remove observavility portion from makefile (if you like)
- Save docker images in local dockerhub repo
- Update docker image name in your deployment yamls if needed
- Add `/ready` in todoapp.
- Add `livenessprobe` and `readynessprobe` in the deployment manifest.

## Test

## Solution
- cd to this directory, run `make relaunch-cluster`.
- All shoudl work.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-4/1-update-strategies-and-prometheus)</i>