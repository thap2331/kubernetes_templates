CLUSTER_NAME=multi-container-pod
NAMESPACE=multi-container-pod-ns

# local development kubernetes cluster
cluster-dev: set-context
	k3d cluster create ${CLUSTER_NAME} -a 3 --api-port localhost:6443

clean-cluster: set-context
	k3d cluster delete ${CLUSTER_NAME}

relaunch-cluster: set-context clean-cluster cluster-dev

deploy: set-context
	echo "Deploy the kubernetes config to local cluster"
	kubectl apply -f deployment.yaml

# Safety to make to ensure you're targeting the k3d cluster 
# and not accidentally a running production cluster
set-context:
	echo "Make sure we don't deploy to the wrong cluster"
	kubectl config set-context ${CLUSTER_NAME}