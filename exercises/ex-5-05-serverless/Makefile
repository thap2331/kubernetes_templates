CLUSTER_NAME=TODOex-5-05

cluster-dev: set-context
	mkdir -p /tmp/k3dvol
	k3d cluster create ${CLUSTER_NAME} \
		--port 8082:30080@agent:0 \
		--port 8081:80@loadbalancer \
		--agents 2 \
		--volume /tmp/k3dvol:/tmp/k3dvol \
		--k3s-arg "--disable=traefik@server:0"
	kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.13.0/serving-crds.yaml
	kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.13.0/serving-core.yaml
	kubectl apply -f https://github.com/knative/net-contour/releases/download/knative-v1.13.0/contour.yaml \
				  -f https://github.com/knative/net-contour/releases/download/knative-v1.13.0/net-contour.yaml
	kubectl patch configmap/config-network \
		--namespace knative-serving \
		--type merge \
		--patch '{"data":{"ingress-class":"contour.ingress.networking.knative.dev"}}'
	kubectl apply -f ./manifests/db-configmap.yaml
	kubectl apply -f ./manifests/postgres-service.yaml
	kubectl apply -f ./manifests/postgres-statefulset.yaml
	kubectl apply -f ./manifests/knative_service.yaml

cluster-dev-skaffold: set-context
	mkdir -p /tmp/k3dvol
	k3d cluster create ${CLUSTER_NAME} \
		--volume /tmp/k3dvol:/tmp/k3dvol \
		-p 8080:80@loadbalancer \
		-p 3000:3000@loadbalancer \
		--agents 2 \
		--api-port localhost:6443
	kubectl create namespace todotest

clean-cluster: set-context
	k3d cluster delete ${CLUSTER_NAME}

relaunch-cluster: clean-cluster cluster-dev

deploy: set-context
	echo "Deploy the kubernetes config to local cluster"
	kubectl apply -f manifests

build-images:
	docker build -t surajkodocker/logreader .
	docker build -t surajkodocker/pingpong:latest  -f Dockerfile.pong .

push-to-docker:
	docker push surajkodocker/pingpong:latest
	docker push surajkodocker/logreader:latest

build-and-push: build-images push-to-docker

set-context:
	echo "Make sure we don't deploy to the wrong cluster"
	kubectl config set-context ${CLUSTER_NAME}
# kubectl config set-context --current --namespace=logtest