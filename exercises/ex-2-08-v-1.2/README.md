# Exercise 2.08
## Prompt
- Create a database and save the todos there. Use Secrets and/or ConfigMaps to have the backend access the database.

## Get started: Copy directory ex-2-04-v-1.1 as ex-2-08-v-1.2

## Hint
- Mock ex-2-06
- Use `kubectl create namespace todotest`

## Test
    - If http://localhost:8081/ root page shows an image and todo app, then we know it works. Refresh after 10 seconds and view the updated image.

## Notes:
- To add a defualt namespace, you have to manually add `kubectl config set-context --current --namespace=<name>`

## Solution
    - cd to this directory, run `make relaunch-cluster` and check http://localhost:8081/ and check again after 10 seconds to see the updated image.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-1/4-introduction-to-storage)</i>