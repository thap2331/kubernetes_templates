# Exercise 4-05 - Local development with Skaffold (instead of GitOps)

## Prompt - Do local devopment using Skaffold
-  Install `skaffold`. Use `curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/v1.0.1/skaffold-linux-amd64 && chmod +x skaffold && sudo mv skaffold /usr/local/bin`

## Hint
- Get started: Copy directory ex-4-05-v-1.9 as ex-4-07-gitops
- cd to this directory
- Make sure to have `skaffold` installed. You can use `skaffold init` to get your `skaffold.yaml`. You can set up different profiles as well.

## Test
- Open a new terminal to see ingress service, `kubectl -n todotest get ing` and get ip address
- Make changes to the app and watch it update

### For ArgoCD (only half baked)
- Get ArgoCD install yaml `wget https://raw.githubusercontent.com/argoproj/argo-cd/v2.0.1/manifests/install.yaml` and update the application root path with the –rootpath option (See more in <i>[Local ArgoCD Blog](https://www.techmanyu.com/setup-a-gitops-deployment-model-on-your-local-development-environment-with-k3s-k3d-and-argocd-4be0f4f30820)</i>)
- Add `kubectl create namespace argocd`
- Add `kubectl apply -f install.yaml -n argocd`
- Update `ingress.yaml` so that path includes
- Update the new way of `apiVersion: networking.k8s.io/v1` and not as recommended in this [local ArgoCD blog](https://www.techmanyu.com/setup-a-gitops-deployment-model-on-your-local-development-environment-with-k3s-k3d-and-argocd-4be0f4f30820)
- I updated the docker tag name while building and pushing images. I did the same in manifests' deployment files as well.
- Access argocd ui in `http://localhost:8081/argocd` (Or, `kubectl -n todotest get ing` and get ip address)
- Use `kubectl -n todotest get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d && echo`
    - User: `admin`

## Test

## Solution
- cd to this directory, run `make relaunch-cluster`
- Get ingress using `kubectl get ing -n todotest`
- Start skaffold `skaffold init`
- Make app changes to see new changes

<i>Source: [Set up](https://skaffold.dev/docs/quickstart/)</i>
<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-4/3-gitops)</i>