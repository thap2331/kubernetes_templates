# Exercise 4-05 - Service Mesh

## Prompt - Service Mesh

## Prereqs
- [Linkerd](https://linkerd.io/2.14/getting-started/#step-1-install-the-cli)

## Hint
- Get started: Copy directory ex-4-07-gitops as ex-5-02-service-mesh
- cd to this directory
- Build and push the docker images
- Add `kubectl apply -f ./manifests/` back to cluster-dev
- Now follow [linkerd's getting starter](https://linkerd.io/2.14/getting-started/)
- Cleanup: Remove argocd from ingress manifest if its there

## Test
- Open a new terminal to see ingress service, `kubectl -n todotest get ing` and get ip address
- Make changes to the app and watch it update

## Test

## Solution
- cd to this directory, run `make relaunch-cluster`
- Get ingress using `kubectl get ing -n todotest`
- Do `linkerd viz dashboard` to get dashboard up

<i>Source: [Set up](https://skaffold.dev/docs/quickstart/)</i>
<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-4/3-gitops)</i>