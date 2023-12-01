CLUSTER_NAME=MYGEN

# local development kubernetes cluster
cluster-dev: set-context
	k3d cluster create ${CLUSTER_NAME} -a 3 --api-port localhost:6443
	docker build -t mygenapp .
	k3d image import -c MYGEN mygenapp
	kubectl apply -f ./manifests/deployment.yaml

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