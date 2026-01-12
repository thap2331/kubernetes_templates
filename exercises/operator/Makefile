CLUSTER_NAME=raycluster1
# kubectl get nodes
cluster-dev: set-context
	k3d cluster create ${CLUSTER_NAME} --agents 1

deploy:
	kubectl apply -f ./manifests/mycrd.yaml

custom-resource-deploy:
	kubectl apply -f ./manifests/greeting.yaml

clean-cluster:set-context
	k3d cluster delete ${CLUSTER_NAME}

set-context:
	echo "Make sure we don't deploy to the wrong cluster"
	kubectl config set-context ${CLUSTER_NAME}