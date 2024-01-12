CLUSTER_NAME=TODOex210

cluster-dev: set-context
	mkdir -p /tmp/k3dvol
	k3d cluster create ${CLUSTER_NAME} --volume /tmp/k3dvol:/tmp/k3dvol -p 8081:80@loadbalancer -p 3000:3000@loadbalancer --agents 2 --api-port localhost:6443
	kubectl create namespace todotest
	kubectl create namespace loki
	helm install prometheus-community/kube-prometheus-stack --generate-name --namespace=loki
	helm repo add grafana https://grafana.github.io/helm-charts
	helm repo update
	helm upgrade --install --namespace=loki loki grafana/loki-stack -f logging-values.yaml --set loki.auth_enabled=false
	kubectl get secret --namespace=loki loki-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
	docker build -t todoapp-image .
	docker build -t imagegenerator-image  -f image-generator.Dockerfile .
	docker build -t cronjob-image  -f cronjob.Dockerfile .
	k3d image import -c ${CLUSTER_NAME} todoapp-image imagegenerator-image cronjob-image
	kubectl apply -f ./manifests/
	kubectl -n loki port-forward service/loki-grafana 3000:80

clean-cluster: set-context
	k3d cluster delete ${CLUSTER_NAME}

relaunch-cluster: clean-cluster cluster-dev

deploy: set-context
	echo "Deploy the kubernetes config to local cluster"
	kubectl apply -f manifests

# Safety to make to ensure you're targeting the k3d cluster 
# and not accidentally a running production cluster
set-context:
	echo "Make sure we don't deploy to the wrong cluster"
	kubectl config set-context ${CLUSTER_NAME}
	kubectl config set-context --current --namespace=todotest