# Exercise 3.08
## Prompt
- Create a CronJob that generates a new todo every 15 seconds.

## Prereqs
- Install [Helm](https://helm.sh/docs/intro/install/)
    - Add Helm the official charts repository
        - `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
        - `helm repo add stable https://charts.helm.sh/stable`
- Install [kube-prometheus-stack](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack)

## Get started: Copy directory ex-2-10-v-1.3-monitoring to ex-3-08-v-1.5-horizontal-scale

## Hint
- Add docker images to public repo in dockerhub
- Update the app to use up cpu utilization
- Delete ingress and update service to loadbalancer in manifests
- I am not deploying `cronjob.yaml`. It is commented on `kustomization.yaml`.
- Remove `storageClassName: local-path` from `postgres-statefulset.yaml`.
- If your postgres logs say `initdb: error: directory "/var/lib/postgresql/data" exists but is not empty`, add subPath configuration in `postgres-statefulset.yaml`.
- Add `horizontalpodautoscaler.yaml`
- Add resource limits to `deployment.yaml`
    -   ```
        resources:
            limits:
                cpu: "150m"
                memory: "100Mi"
        ```

## Test
    - Open http://localhost:8081/.

## Notes:
- To add a defualt namespace, you have to manually add `kubectl config set-context --current --namespace=<name>`
- Grafana and url for loki data source
    - All apps and logging in a same namespace. Grafana id is `admin` and password is `prom-operator`. The loki url is `http://loki.loki:3100`.
    - Apps in one namespace and logging in another namespace. Grafana id is `admin` and password is from `kubectl get secret --namespace=loki loki-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo`. The loki url is `http://{service-name}.{namespace}:3100`, i.e. `http://loki.loki:3100`.

## Solution
- cd to this directory (you don't have to).
- Save docker images to be used in a public repo.
- Run the cluster: `make cluster-dev`
- See if this directory would be triggered on github actions [workflow file](./../../.github/workflows/ex-3-08.yaml). Create a commit and push. This should trigger the pipeline (given you have the credentials set up well.)
- Wait for the deployment to show up in goolge cloud console.
- Run `http://{IP-ADDREDD}:3100/run_core` to trigger the cpu utilization.
- Go to google cloud console and watch the pods scale up and down.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-3/3-gke-features)</i>