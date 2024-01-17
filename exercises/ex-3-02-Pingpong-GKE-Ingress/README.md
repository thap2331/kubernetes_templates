# Exercise 3.02: Introduction to Google Kubernetes Engine - Ingress

## Prompt: Connect with GKE and use a ingress service for your log output and pong apps

## Get started:
- Install [gke](https://cloud.google.com/sdk/docs/install)
    - Initialize using `gcloud init`
- Copy directory ex-3-01-Pingpong-GKE as ex-3-02-Pingpong-GKE-Ingress

## Prereqs
- Get your [google cloud set up well](https://cloud.google.com/sdk/docs/install).
- Docker
    - Create a dockerhub account.
    - Create a public docker repository.
    - Configure docker in cli, i.e.,`docker login --username`

## Hint
- Update pong app so that it has root path. When an app is deployed and attached to ingress, the GKE checks for health by hitting the root path.
- Update the docker image. 
- Push the updated docker images to a public dockerhub repo so that you can pull it easily.
- Update `logoutput-service.yaml` and `pong-service.yaml` services from `LoadBalancer` to `NodePort`.  
- Add ingress to manifests. (Hint: You can copy from `ex-2-07`. You can also remove extra path, `/count`).
- See the ingress
    - `kubectl get ing -n logtest`
- Sometimes deleting the deployment in GKE and applying manifests again worked. If the ingress does not have any IP address, this method worked well.

## Tests
- This `http://{{ INGRESS-IP }}:3001/pingpong` should show pong count.
- This `http://{{ INGRESS-IP }}:3001/now` should show you the time now and count.


## Solution
- cd to this directory
- Run `gcloud container clusters create suraj-test-gke --disk-type "pd-balanced" --disk-size "20" --num-nodes "2" --zone=us-west1-b --cluster-version=1.29`
    - wait for the cluster to come alive
- Set the kubeconfig to point in the right direction. Run `gcloud container clusters get-credentials suraj-test-gke --zone=us-west1-b`
- Build docker images that will match the name of images in deployment yaml files. Now push the images to dockerhub public repo.
    - See [makefile](./Makefile) for more.
- Run deploy by using below
    - `kubectl create namespace logtest`
    - `kubectl apply -f ./manifests/`
- Get ingress: `kubectl get ing -n logtest`
- Pick the ADDRESS with port and run: `http://{{ INGRESS-IP }}:3001/pingpong`, e.g., http://35.197.62.147:3001/pingpong. This should start the counter. Now run: `http://{{ EXTERNAL-IP }}:3001/now`. This should show you the time and count.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-3/1-introduction-to-gke)</i>