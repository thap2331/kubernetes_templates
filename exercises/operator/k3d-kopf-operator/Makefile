create-cluster:
	#Create a cluster with registry enabled (if not already)
	k3d cluster create my-cluster --registry-create my-registry.localhost:5000

docker:
	#Tag and push to k3d registry
	docker build -t my-operator .
	docker run --rm my-operator
	docker tag my-operator my-registry.localhost:5000/my-operator:latest
	docker push my-registry.localhost:5000/my-operator:latest

apply-crd-deploy-operator:
	kubectl apply -f crd.yaml
	kubectl apply -f deploy.yaml
	kubectl apply -f greeting.yaml

cleanup:
	kubectl delete -f greeting.yaml
	kubectl delete -f deploy.yaml
	kubectl delete -f crd.yaml
	k3d cluster delete my-cluster