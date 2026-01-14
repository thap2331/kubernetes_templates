CLUSTER_NAME=HPGRay
GRAFANA_PASSWORD=password
MONITORING_NAMESPACE=monitoring
kuberay_version = 1.5.1

cluster-dev: set-context
	mkdir -p /tmp/k3dvol
	k3d cluster create ${CLUSTER_NAME} --registry-create ray-registry:0.0.0.0:5550 --agents 2 --wait \
	--volume /tmp/k3dvol:/tmp/k3dvol \
	-p 10001:10001@loadbalancer -p 6379:6379@loadbalancer \
	--k3s-arg '--kubelet-arg=eviction-hard=imagefs.available<1%,nodefs.available<1%@agent:*' \
	--k3s-arg '--kubelet-arg=eviction-minimum-reclaim=imagefs.available=1%,nodefs.available=1%@agent:*' \
	--k3s-arg '--kubelet-arg=eviction-hard=imagefs.available<1%,nodefs.available<1%@server:0' \
	--k3s-arg '--kubelet-arg=eviction-minimum-reclaim=imagefs.available=1%,nodefs.available=1%@server:0'
	helm repo add stable https://charts.helm.sh/stable
	helm repo update

## install kuberay operator using quickstart manifests
kuberay-operator:
	helm repo add kuberay https://ray-project.github.io/kuberay-helm/
	helm repo update
	helm install kuberay-operator kuberay/kuberay-operator --version $(kuberay_version) --wait --debug > /dev/null
	kubectl get pods

raycluster-multiple-clusters:
#Deploy a sample RayCluster CR from the KubeRay Helm chart repo:
#helm install raycluster kuberay/ray-cluster --version ${kuberay_version}
	kubectl get namespace ray-cluster-1 || kubectl create namespace ray-cluster-1 
	kubectl apply -f ./manifests/ray-cluster1.yaml 
	kubectl get namespace ray-cluster-2 || kubectl create namespace ray-cluster-2
	kubectl apply -f ./manifests/ray-cluster2.yaml

submit-rayjob-multiple-clusters1:
	kubectl -n ray-cluster-1 port-forward service/raycluster-kuberay-head-svc 8265:8265 > /dev/null &
	ray job submit --address http://localhost:8265 --working-dir ./ray_job_files/ -- python ray_testjob.py

submit-rayjob-multiple-clusters2:
	kubectl -n ray-cluster-2 port-forward service/raycluster-kuberay-head-svc 8266:8265 > /dev/null &
	ray job submit --address http://localhost:8266 --working-dir ./ray_job_files/ -- python ray_testjob.py


raycluster-one-cluster:
#Deploy a sample RayCluster CR from the KubeRay Helm chart repo:
#helm install raycluster kuberay/ray-cluster --version ${kuberay_version}
	kubectl create namespace ray-cluster-1
	kubectl apply -f ./manifests/ray-cluster.yaml

# Once the RayCluster CR has been created, you can view it by running:
	kubectl get rayclusters
# View the pods in the RayCluster named "raycluster-kuberay"
	kubectl get pods --selector=ray.io/cluster=raycluster-kuberay

rayjob:
	kubectl apply -f https://raw.githubusercontent.com/ray-project/kuberay/v1.4.2/ray-operator/config/samples/ray-job.sample.yaml

delete-rayjob:
	kubectl delete -f https://raw.githubusercontent.com/ray-project/kuberay/v1.4.2/ray-operator/config/samples/ray-job.sample.yaml

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