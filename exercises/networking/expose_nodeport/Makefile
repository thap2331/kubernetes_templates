CLUSTER_NAME=NETWORKPREP

# inspired from: https://github.com/k3d-io/k3d/blob/main/docs/usage/exposing_services.md
cluster-dev: set-context
	k3d cluster create ${CLUSTER_NAME} -p "8082:30080@agent:0" --agents 2 --api-port localhost:6550
	kubectl apply -f ./manifests/nginx.yaml
	kubectl apply -f ./manifests/nginx_service.yaml

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