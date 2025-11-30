CLUSTER_NAME=OPERATOR-TUTORIAL
# kubectl get nodes
cluster-dev: set-context
	k3d cluster create my-cluster --agents 1

deploy:
	kubectl apply -f ./manifests/mycrd.yaml
custom-resource-deploy:
	kubectl apply -f ./manifests/greeting.yaml


set-context:
	echo "Make sure we don't deploy to the wrong cluster"
	kubectl config set-context ${CLUSTER_NAME}