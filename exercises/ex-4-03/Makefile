CLUSTER_NAME=TODOex403

# helm repo add stable https://charts.helm.sh/stable
# helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
# kubectl apply -n todotest -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml
# kubectl apply -n todotest -f https://raw.githubusercontent.com/argoproj/argo-rollouts/master/manifests/install.yaml

cluster-dev: set-context #build-images push-to-docker
	mkdir -p /tmp/k3dvol
	k3d cluster create ${CLUSTER_NAME} --volume /tmp/k3dvol:/tmp/k3dvol -p 8081:80@loadbalancer -p 3000:3000@loadbalancer --agents 2 --api-port localhost:6443
	kubectl create namespace todotest
	kubectl create namespace loki
	helm install prometheus-community/kube-prometheus-stack --generate-name --namespace=loki
	helm repo add grafana https://grafana.github.io/helm-charts
	helm repo update
	helm upgrade --install loki --namespace=loki grafana/loki-stack --set loki.auth_enabled=false --set grafana.enabled=true
	kubectl get secret --namespace=loki loki-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
	kubectl create namespace argo-rollouts
	kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml
	kubectl apply -f ./manifests/
	kubectl apply -n todotest -f rollout.yaml
	kubectl -n loki port-forward service/loki-grafana 3000:80

clean-cluster: set-context
	k3d cluster delete ${CLUSTER_NAME}

relaunch-cluster: clean-cluster cluster-dev

deploy: set-context
	echo "Deploy the kubernetes config to local cluster"
	kubectl apply -f manifests

build-images:
	docker build -t surajkodocker/todo:ex-4-03 .
	docker build -t surajkodocker/imagegenerator:ex-4-03 -f image-generator.Dockerfile .
	docker build -t surajkodocker/cronjob:ex-4-03 -f cronjob.Dockerfile .

push-to-docker:
	docker push surajkodocker/todo:ex-4-03
	docker push surajkodocker/imagegenerator:ex-4-03
	docker push surajkodocker/cronjob:ex-4-03

set-context:
	echo "Make sure we don't deploy to the wrong cluster"
	kubectl config set-context ${CLUSTER_NAME}
	kubectl config set-context --current --namespace=todotest