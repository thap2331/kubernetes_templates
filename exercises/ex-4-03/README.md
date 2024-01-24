# Exercise 4-03

## Prompt - See data in prometheus

## Prereqs
- Install [Helm](https://helm.sh/docs/intro/install/)
    - Add Helm the official charts repository
        - `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
        - `helm repo add stable https://charts.helm.sh/stable`
- Install [kube-prometheus-stack](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack)

## Hint
- Get started: Copy directory ex-4-02-v-1.7-probes to ex-4-03
- Update `deployment.yaml` to `kind: Rollout`. Make other changes to `canary releases`.
- Add observavility portion in makefile from ex-2-10-v-1.3-monitoring
- Update docker images and push them to public dockerhub repo
- Update docker image name in your deployment yamls
- If `localhost:3000` is not working, try `http://127.0.0.1:3000/`
- Apply `kubectl apply -n todotest -f rollout.yaml`.
- I am not sure about query. Skipping it for now so that I can get through the material as I am in rush.

## Test

## Solution
- cd to this directory, run `make relaunch-cluster`.
- All should work.
- If `localhost:3000` is not working, then try `http://127.0.0.1:3000/`

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-4/1-update-strategies-and-prometheus)</i>