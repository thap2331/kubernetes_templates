# Exercise 2.02
## Prompt
- Create a namespace for the project and move everything related to the project to that namespace.

## Get started: Copy directory ex-2-02-v-1 as ex-2-04-v-1.1

## Hint
- Add a namespace right after creating the cluster.
- Use `kubectl create namespace todotest`

## Test
    - If http://localhost:8081/ root page shows an image and todo app, then we know it works. Refresh after 10 seconds and view the updated image.

## Notes:
- To add a defualt namespace, you have to manually add `kubectl config set-context --current --namespace=<name>`

## Solution
    - cd to this directory, run `make relaunch-cluster` and check http://localhost:8081/ and check again after 10 seconds to see the updated image.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-1/4-introduction-to-storage)</i>