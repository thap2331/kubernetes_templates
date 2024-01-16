CLUSTER_NAME=suraj-test-gke

# local development kubernetes cluster
cluster-dev:
	gcloud container clusters create ${CLUSTER_NAME} --disk-type "pd-balanced" --disk-size "20" --num-nodes "2" --zone=us-west1-b --cluster-version=1.29

clean-cluster:
	gcloud container clusters delete ${CLUSTER_NAME} --zone=us-west1-b

deploy:
	kubectl create namespace logtest
	kubectl apply -f ./manifests/

build-images:
	docker build -t surajkodocker/logreader .
	docker build -t surajkodocker/pingpong:latest  -f Dockerfile.pong .

push-to-docker:
	docker push surajkodocker/pingpong:latest
	docker push surajkodocker/logreader:latest