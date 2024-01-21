CLUSTER_NAME=todoex308

cluster-dev:
	gcloud container clusters create ${CLUSTER_NAME} --disk-type "pd-balanced" --disk-size "20" --num-nodes "2" --zone=us-west1-b --cluster-version=1.29

clean-cluster:
	gcloud container clusters delete ${CLUSTER_NAME} --zone=us-west1-b

relaunch-cluster: clean-cluster cluster-dev

deploy:
	kubectl apply -f ./manifests/

build-images:
	docker build -t surajkodocker/todo .
	docker build -t surajkodocker/imagegenerator:latest -f image-generator.Dockerfile .

push-to-docker:
	docker push surajkodocker/todo:latest
	docker push surajkodocker/imagegenerator:latest