# Exercise 2.10
## Prompt
- Create a CronJob that generates a new todo every 15 seconds.

## Get started: Copy directory ex-2-08-v-1.2 to ex-2-10

## Hint
- Mock ex-2-08-v-1.2
- Use `kubectl create namespace todotest`
- Add necessary python files for cronjob. For testing, you can make the cron job to add a new task every minute.
- Add a new docker for a cronjob
- Add a new deployment for a cronjob

## Test
    - Open http://localhost:8081/. Wait for 5 seconds if it says "postgres-svc" is not found yet. Wait 1 minute and see if the new todo task is added. If so, then we know it works.

## Notes:
- To add a defualt namespace, you have to manually add `kubectl config set-context --current --namespace=<name>`

## Solution
    - cd to this directory, run `make relaunch-cluster` and check http://localhost:8081/. Wait 1 minute and see if the new todo task is added.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-2/4-statefulsets-and-jobs)</i>