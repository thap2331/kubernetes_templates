CLUSTER_NAME=LogPONG201

# local development kubernetes cluster
cluster-dev: set-context
	k3d cluster create ${CLUSTER_NAME} -p "8081:80@loadbalancer" --agents 2 --api-port localhost:6550
	docker build -t logreader .
	docker build -t pingpong-image  -f Dockerfile.pong .
	k3d image import -c ${CLUSTER_NAME} logreader pingpong-image
	kubectl apply -f ./manifests/

clean-cluster: set-context
	k3d cluster delete ${CLUSTER_NAME}

relaunch-cluster: set-context clean-cluster cluster-dev

deploy: set-context
	echo "Deploy the kubernetes config to local cluster"
	kubectl apply -f manifests

# Safety to make to ensure you're targeting the k3d cluster 
# and not accidentally a running production cluster
set-context:
	echo "Make sure we don't deploy to the wrong cluster"
	kubectl config set-context ${CLUSTER_NAME}