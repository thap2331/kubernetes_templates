CLUSTER_NAME=HPGRay
GRAFANA_PASSWORD=password
NAMESPACE=ray
MONITORING_NAMESPACE=monitoring
kuberay_version = 1.5.0


cluster-dev: set-context
	mkdir -p /tmp/k3dvol
	k3d cluster create ${CLUSTER_NAME} --registry-create ray-registry:0.0.0.0:5550 --agents 2 --wait \
	--volume /tmp/k3dvol:/tmp/k3dvol \
	-p 10001:10001@loadbalancer -p 6379:6379@loadbalancer \
	--k3s-arg '--kubelet-arg=eviction-hard=imagefs.available<1%,nodefs.available<1%@agent:*' \
	--k3s-arg '--kubelet-arg=eviction-minimum-reclaim=imagefs.available=1%,nodefs.available=1%@agent:*' \
	--k3s-arg '--kubelet-arg=eviction-hard=imagefs.available<1%,nodefs.available<1%@server:0' \
	--k3s-arg '--kubelet-arg=eviction-minimum-reclaim=imagefs.available=1%,nodefs.available=1%@server:0'
	kubectl create namespace ${NAMESPACE}
	helm repo add stable https://charts.helm.sh/stable
	helm repo update
	make kuberay
	make raycluster


## install kuberay operator using quickstart manifests
kuberay:
	helm repo add kuberay https://ray-project.github.io/kuberay-helm/
	helm repo update
#Install both CRDs and KubeRay operator v1.4.2.
	helm install kuberay-operator kuberay/kuberay-operator --version $(kuberay_version) --namespace ${NAMESPACE} --wait --debug > /dev/null
#Confirm that the operator is running in the namespace default.
	kubectl get pods -n ${NAMESPACE}

raycluster:
#Deploy a sample RayCluster CR from the KubeRay Helm chart repo:
	helm install raycluster -n ${NAMESPACE} kuberay/ray-cluster --version 1.5.0
# Once the RayCluster CR has been created, you can view it by running:
	kubectl get rayclusters -n ${NAMESPACE}
# View the pods in the RayCluster named "raycluster-kuberay"
	kubectl get pods --selector=ray.io/cluster=raycluster-kuberay -n ${NAMESPACE}

rayjob:
	kubectl -n ${NAMESPACE} apply -f https://raw.githubusercontent.com/ray-project/kuberay/v1.4.2/ray-operator/config/samples/ray-job.sample.yaml

delete-rayjob:
	kubectl -n ${NAMESPACE} delete -f https://raw.githubusercontent.com/ray-project/kuberay/v1.4.2/ray-operator/config/samples/ray-job.sample.yaml

clean-cluster: set-context
	k3d cluster delete ${CLUSTER_NAME}

relaunch-cluster: clean-cluster cluster-dev

deploy: set-context
	echo "Deploy the kubernetes config to local cluster"
	kubectl apply -f manifests

build-images:
	docker build -t surajkodocker/todo:ex-4-02 .
	docker build -t surajkodocker/imagegenerator:ex-4-02 -f image-generator.Dockerfile .
	docker build -t surajkodocker/cronjob:ex-4-02 -f cronjob.Dockerfile .

push-to-docker:
	docker push surajkodocker/todo:ex-4-02
	docker push surajkodocker/imagegenerator:ex-4-02
	docker push surajkodocker/cronjob:ex-4-02

set-context:
	echo "Make sure we don't deploy to the wrong cluster"
	kubectl config set-context ${CLUSTER_NAME}
	kubectl config set-context --current --namespace=${NAMESPACE}