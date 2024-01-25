CLUSTER_NAME=LogPONG401

# local development kubernetes cluster
cluster-dev: set-context build-images push-to-docker
	k3d cluster create ${CLUSTER_NAME} -p "8082:80@loadbalancer" --agents 2 --api-port localhost:6550
	kubectl create namespace logtest
	kubectl apply -f ./manifests/

clean-cluster: set-context
	k3d cluster delete ${CLUSTER_NAME}

relaunch-cluster: set-context clean-cluster cluster-dev

deploy: set-context
	echo "Deploy the kubernetes config to local cluster"
	kubectl apply -f manifests

build-images:
	docker build -t surajkodocker/logreader:ex-4-01 .
	docker build -t surajkodocker/pingpong:ex-4-01 -f Dockerfile.pong .

push-to-docker:
	docker push surajkodocker/logreader:ex-4-01
	docker push surajkodocker/pingpong:ex-4-01

# Safety to make to ensure you're targeting the k3d cluster 
# and not accidentally a running production cluster
set-context:
	echo "Make sure we don't deploy to the wrong cluster"
	kubectl config set-context ${CLUSTER_NAME}
	kubectl config set-context --current --namespace=logtest