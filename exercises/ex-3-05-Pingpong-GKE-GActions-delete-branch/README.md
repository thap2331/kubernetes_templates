# Exercise 3.05: Deployment Pipeline (GitHub Actions)

## Prompt: Configure workflow file that will clean the environment once a branch is deleted

## Get started:
- Copy directory ex-3-04-Pingpong-GKE-GActions-each-branch as ex-3-05-Pingpong-GKE-GActions-delete-branch

## Prereqs
- Get your [google cloud set up well](https://cloud.google.com/sdk/docs/install).
- Docker

## Hint
- Create a new branch for this.
- Add `.github/workflows/delete-branch.yaml`. This is where the bulk of our work is going to be. See more in [devopswithkubernetes.com](https://devopswithkubernetes.com/part-3/2-deployment-pipeline).
- In `.github/workflows/delete-branch.yaml`, use it once to create a deployment based on the branch name. Once the deployment to GKE is completed, retract those changes.
- Now configure `.github/workflows/delete-branch.yaml` so that this workflow will run once a branch is deleted.
    - To get the name of a deleted branch, use `github.event.ref`.

## Tests
- Merge this branch.
- Delete this branch, check if the workflow ran, and check if it deleted the namespace you desired in GKE.

## Solution
- Make a branch. Push some small changes.
- Merge the branch.
- Delete the branch.
- See a workflow pipeline triggered.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-3/2-deployment-pipeline)</i>