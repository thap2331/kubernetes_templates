# Exercise 2.10
## Prompt
- Create a CronJob that generates a new todo every 15 seconds.

## Prereqs
- Install [Helm](https://helm.sh/docs/intro/install/)
    - Add Helm the official charts repository
        - `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
        - `helm repo add stable https://charts.helm.sh/stable`
- Install [kube-prometheus-stack](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack)

## Get started: Copy directory ex-2-08-v-1.2 to ex-2-10

## Hint
- Mock ex-2-08-v-1.2
- Use `kubectl create namespace todotest`
- Add necessary python files for cronjob. For testing, you can make the cron job to add a new task every minute.
- Add a new docker for a cronjob
- Add a new deployment for a cronjob
- Ensure your app is logging outputs.

## Test
    - Open http://localhost:8081/.

## Notes:
- To add a defualt namespace, you have to manually add `kubectl config set-context --current --namespace=<name>`
- Grafana and url for loki data source
    - All apps and logging in a same namespace. Grafana id is `admin` and password is `prom-operator`. The loki url is `http://loki.loki:3100`.
    - Apps in one namespace and logging in another namespace. Grafana id is `admin` and password is from `kubectl get secret --namespace=loki loki-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo`. The loki url is `http://{service-name}.{namespace}:3100`, i.e. `http://loki.loki:3100`.

## Solution
    - cd to this directory, run `make relaunch-cluster`. The terminal should run and show `Forwarding from 127.0.0.1:3000 -> 3000.....` at the end. Check http://localhost:8081/. Then check `http://localhost:8081/` and log in using `admin` and password which is printed on stdout. (Alternatively, you can do `kubectl get secret --namespace=loki loki-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo` ).

    - Now you can add loki by adding this url: `http://loki.loki:3100`

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-2/5-monitoring)</i>