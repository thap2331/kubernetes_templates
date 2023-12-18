CLUSTER_NAME=TODOv102

# local development kubernetes cluster
cluster-dev: set-context
	mkdir -p /tmp/k3dvol
	k3d cluster create ${CLUSTER_NAME} --volume /tmp/k3dvol:/tmp/k3dvol -p 8081:80@loadbalancer --agents 2 --api-port localhost:6443
	kubectl create namespace todotest
	docker build -t todoapp-image .
	docker build -t imagegenerator-image  -f image-generator.Dockerfile .
	k3d image import -c ${CLUSTER_NAME} todoapp-image imagegenerator-image
	kubectl apply -f ./manifests/

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