## Ray dashboard from grafana and prometheus

<!-- https://docs.ray.io/en/latest/cluster/kubernetes/k8s-ecosystem/prometheus-grafana.html#kuberay-prometheus-grafana -->

- `make cluster-dev`
    - This will start a cluster, install prometheus, install kuberay operator.
- `make raycluster`
<!-- Forward the port of the Prometheus metrics endpoint. -->
	kubectl -n ray port-forward service/raycluster-embed-grafana-head-svc metrics
<!-- Check metrics in a new terminal. -->
	curl localhost:8080