cluster-dev:
	minikube start
	minikube kubectl -- get pods -A
	minikube status

kubeflow-deploy:
	kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=2.15.0"
	kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
	kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/dev?ref=2.15.0"

kubeflow-storage:
	kubectl apply -f manifests/local-storage.yaml
	minikube mount ./test_data:/data/kflow

see-all-pods:
	minikube kubectl -- get pods -A

kubeflow-ui:
	kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80 > /dev/null &

pipeline_image:
	eval $(minikube docker-env)
	docker build -t kflow:latest -f Dockerfile .

kill-proxy:
	kubectl scale deployment proxy-agent -n kubeflow --replicas=0

clean-cluster:
	echo "Deleting the cluster"
	minikube delete --all

relaunch-cluster: clean-cluster cluster-dev

deploy:
	kubectl apply -f ./manifests/