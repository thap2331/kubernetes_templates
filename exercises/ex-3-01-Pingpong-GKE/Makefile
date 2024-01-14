CLUSTER_NAME=suraj-test-gke

# local development kubernetes cluster
cluster-dev: set-context
	gcloud container clusters create ${CLUSTER_NAME} --disk-type "pd-balanced" --disk-size "20" --num-nodes "3" --zone=us-west1 --cluster-version=1.29


# k3d cluster create ${CLUSTER_NAME} -p "8081:80@loadbalancer" --agents 2 --api-port localhost:6550
# kubectl create namespace logtest
# docker build -t logreader .
# docker build -t pingpong-image  -f Dockerfile.pong .
# k3d image import -c ${CLUSTER_NAME} logreader pingpong-image
# kubectl apply -f ./manifests/


clean-cluster: set-context
	gcloud container clusters delete ${CLUSTER_NAME} --zone=us-west1

relaunch-cluster: set-context clean-cluster cluster-dev

deploy: set-context
	echo "Deploy the kubernetes config to local cluster"
	kubectl apply -f manifests

# Safety to make to ensure you're targeting the k3d cluster 
# and not accidentally a running production cluster
set-context:
	echo "Make sure we don't deploy to the wrong cluster"
	kubectl config set-context ${CLUSTER_NAME}
	kubectl config set-context --current --namespace=logtest