CLUSTER_NAME=TODOex402

cluster-dev: set-context build-images push-to-docker
	mkdir -p /tmp/k3dvol
	k3d cluster create ${CLUSTER_NAME} --volume /tmp/k3dvol:/tmp/k3dvol -p 8081:80@loadbalancer -p 3000:3000@loadbalancer --agents 2 --api-port localhost:6443
	kubectl create namespace todotest
	kubectl apply -f ./manifests/

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
	kubectl config set-context --current --namespace=todotest