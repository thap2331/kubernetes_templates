# Exercise 3.04: Deployment Pipeline (GitHub Actions)

## Prompt: Configure env for each branch via GitHub Actions

## Get started:
- Copy directory ex-3-03-Pingpong-GKE-GitHub-Actions as ex-3-04-Pingpong-GKE-GActions-each-branch

## Prereqs
- Get your [google cloud set up well](https://cloud.google.com/sdk/docs/install).
- Docker

## Hint
- Configure your google service account with github actions. Keep these two github repo secrets, `GKE_PROJECT` and `GKE_SA_KEY`.
- Add `.github/workflows/main.yaml`. This is where the bulk of our work is going to be. See more in [devopswithkubernetes.com](https://devopswithkubernetes.com/part-3/2-deployment-pipeline)
- I skipped keeping the docker images in Google Cloud step in github actions. Instead, I kept the docker images in dockerhub public repo.

## Tests
- Start with `/pingpong`. This `http://{{ INGRESS-IP }}:3001/pingpong` should show pong count.
- This `http://{{ INGRESS-IP }}:3001/now` should show you the time now and count.


## Solution
- cd to this directory
- Run `gcloud container clusters create suraj-test-gke --disk-type "pd-balanced" --disk-size "20" --num-nodes "2" --zone=us-west1-b --cluster-version=1.29`
    - wait for the cluster to come alive
- Add two github repo secrets, `GKE_PROJECT` and `GKE_SA_KEY`.
- Update the docker images name in deployment apps.
- Make a push to your repo so the the deployment pipeline is kicked off.
- Get external ingress address by using `kubectl get ing -n logtest`.
- Pick the ADDRESS with port and run: `http://{{ INGRESS-IP }}:3001/pingpong`, e.g., http://35.197.62.147:3001/pingpong. This should start the counter. Now run: `http://{{ EXTERNAL-IP }}:3001/now`. This should show you the time and count.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-3/2-deployment-pipeline)</i>