# Exercise 2.08
## Prompt
- Create a database and save the todos there. Use Secrets and/or ConfigMaps to have the backend access the database.

## Get started: Copy directory ex-2-04-v-1.1 as ex-2-08-v-1.2

## Hint
- Mock ex-2-07
- Use `kubectl create namespace todotest`
- Add files to manifests to add a stateful postgres database, db-configmaps, and postgres service
- Update the todo app so that we refer to database instead of in memory json file

## Test
    - Open http://localhost:8081/. Now go delete both todo app pod and postgres pod. Once both pods are back check http://localhost:8081/. If http://localhost:8081/ root page shows an image and todo app, then we know it works.

## Notes:
- To add a defualt namespace, you have to manually add `kubectl config set-context --current --namespace=<name>`

## Solution
    - cd to this directory, run `make relaunch-cluster` and check http://localhost:8081/. Now go delete both todo app pod and postgres pod. Once both pods are back check http://localhost:8081/.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-2/4-statefulsets-and-jobs)</i>