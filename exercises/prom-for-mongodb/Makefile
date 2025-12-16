CLUSTER_NAME=PROM-FOR-MONGODB

# kubectl get nodes
cluster-dev: set-context
	k3d cluster create ${CLUSTER_NAME} \
		--servers 1 \
		--agents 2 \
		--api-port 6443 \
		--port "8080:80@loadbalancer" \
		--port "8443:443@loadbalancer"

prom-operator:
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	helm repo add stable https://charts.helm.sh/stable
	helm repo add grafana https://grafana.github.io/helm-charts
	helm repo update
	helm install prometheus-stack prometheus-community/kube-prometheus-stack \
		--set prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues=false \
		--set prometheus.prometheusSpec.podMonitorSelectorNilUsesHelmValues=false \
		--set prometheus-node-exporter.hostRootFsMount.enabled=false
	kubectl get all

mongodb:
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	helm repo update
	helm install mongodb-exporter prometheus-community/prometheus-mongodb-exporter


deploy: set-context
	kubectl apply -f ./manifests/mongodb.yaml
	kubectl apply -f ./manifests/prometheus.yaml
	kubectl apply -f ./manifests/values.yaml

set-context:
	echo "Make sure we don't deploy to the wrong cluster"
	kubectl config set-context ${CLUSTER_NAME}

clean-cluster: set-context
	k3d cluster delete ${CLUSTER_NAME}