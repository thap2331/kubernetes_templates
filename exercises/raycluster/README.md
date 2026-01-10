# Using k3d for ray: RayCluster Quickstart

## Prereqs
- Activate pipenv if using pipenv. I am using pipenv for this project.
- `pip3 install 'ray[default]'`
- Install [helm for ubuntu](https://helm.sh/docs/intro/install/#from-apt-debianubuntu)
- Follow this [article](https://medium.com/@munza/local-kubernetes-with-k3d-helm-dashboard-6510d906431b)

## Steps to mimic
- `make cluster-dev`

#### Submit a Ray job to the RayCluster using ray job submission SDK

- `kubectl -n ray get service raycluster-kuberay-head-svc`
- `kubectl -n ray port-forward service/raycluster-kuberay-head-svc 8265:8265 > /dev/null &`
- `ray job submit --address http://localhost:8265 -- python -c "import ray; ray.init(); print(ray.cluster_resources())"`

## Tips

-- see pid
`sudo lsof -i TCP:8265`

-- Kill process
`sudo kill -9 <pid>`



## Method 1: Execute a Ray job in the head Pod
- `export HEAD_POD=$(kubectl get pods --selector=ray.io/node-type=head -o custom-columns=POD:metadata.name -n ray --no-headers)`
- `kubectl -n ray exec -it $HEAD_POD -- python -c "import ray; ray.init(); print(ray.cluster_resources())"`


## Method 2: Submit a Ray job to the RayCluster using ray job submission SDK

- `kubectl -n ray get service raycluster-kuberay-head-svc`
- `kubectl -n ray port-forward service/raycluster-kuberay-head-svc 8265:8265 > /dev/null &`
- `ray job submit --address http://localhost:8265 -- python -c "import ray; ray.init(); print(ray.cluster_resources())"`



# Using k3d for ray: RayJob Quickstart


## Prereqs
- Activate pipenv if using pipenv. I am using pipenv for this project.
- `pip3 install 'ray[default]'`
- Install [helm for ubuntu](https://helm.sh/docs/intro/install/#from-apt-debianubuntu)
- Follow this [article](https://medium.com/@munza/local-kubernetes-with-k3d-helm-dashboard-6510d906431b)

## Steps to mimic
- `make cluster-dev`
- `make rayjob`
- Watch them pods get ready for raycluster: `kubectl get pods --selector=ray.io/cluster=raycluster-kuberay -n ray --watch`

<!-- --Step 4.1: List all RayJob custom resources in the `ray` namespace. -->
- `kubectl -n ray get rayjob`

- `kubectl -n ray get raycluster`

- `kubectl -n ray get pods`

- `kubectl -n ray get rayjobs.ray.io rayjob-sample -o jsonpath='{.status.jobStatus}'`
<!-- [Expected output]: "SUCCEEDED" -->
- `kubectl -n ray get rayjobs.ray.io rayjob-sample -o jsonpath='{.status.jobDeploymentStatus}'`
<!-- [Expected output]: "Complete" -->
- `kubectl -n ray logs -l=job-name=rayjob-sample`

<!-- Delete the RayJob -->
- `make delete-rayjob`

<!-- Create a RayJob with shutdownAfterJobFinishes set to true -->
- `kubectl -n ray apply -f https://raw.githubusercontent.com/ray-project/kuberay/v1.4.2/ray-operator/config/samples/ray-job.shutdown.yaml`

<!-- # Wait until `jobStatus` is `SUCCEEDED` and `jobDeploymentStatus` is `Complete`. -->
kubectl -n ray get rayjobs.ray.io rayjob-sample-shutdown -o jsonpath='{.status.jobDeploymentStatus}'
kubectl -n ray get rayjobs.ray.io rayjob-sample-shutdown -o jsonpath='{.status.jobStatus}'

<!-- # List the RayCluster custom resources in the `default` namespace. The RayCluster -->
<!-- # associated with the RayJob `rayjob-sample-shutdown` should be deleted. -->
kubectl -n ray get raycluster

<!-- # Step 10.1: Delete the RayJob -->
kubectl -n ray delete -f https://raw.githubusercontent.com/ray-project/kuberay/v1.4.2/ray-operator/config/samples/ray-job.shutdown.yaml


# Using k3d for ray: RayService Quickstart

## Prereqs
- This guide mainly focuses on the behavior of KubeRay v1.4.2 and Ray 2.46.0. (see more on [ray guide](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/rayservice-quick-start.html))
- Activate pipenv if using pipenv. I am using pipenv for this project.
- `pip3 install 'ray[default]'`
- Install [helm for ubuntu](https://helm.sh/docs/intro/install/#from-apt-debianubuntu)
- Follow this [article](https://medium.com/@munza/local-kubernetes-with-k3d-helm-dashboard-6510d906431b)

## Steps to mimic
- `make cluster-dev`
<!-- install rayservice -->
- `kubectl -n ray apply -f https://raw.githubusercontent.com/ray-project/kuberay/v1.4.2/ray-operator/config/samples/ray-service.sample.yaml`

<!-- Verify the Kubernetes cluster status -->
- `kubectl -n ray get rayservices`
- `kubectl -n ray get raycluster`
- `kubectl -n ray get pods -l=ray.io/is-ray-node=yes`
<!-- # Step 4.4: Check the `Ready` condition of the RayService. -->
<!-- # The RayService is ready to serve requests when the condition is `True`. -->
- `kubectl -n ray describe rayservices.ray.io rayservice-sample`
- `kubectl -n ray get services`
- `kubectl -n ray run curl --image=radial/busyboxplus:curl -i --tty`

# Train a PyTorch model on Fashion MNIST with CPUs on Kubernetes

## Prereqs
- https://docs.ray.io/en/latest/cluster/kubernetes/examples/mnist-training-example.html#kuberay-mnist-training-example
- Activate pipenv if using pipenv. I am using pipenv for this project.
- `pip3 install 'ray[default]'`
- Install [helm for ubuntu](https://helm.sh/docs/intro/install/#from-apt-debianubuntu)
- Follow this [article](https://medium.com/@munza/local-kubernetes-with-k3d-helm-dashboard-6510d906431b)

## Steps to mimic
- `make cluster-dev`
- `curl -LO https://raw.githubusercontent.com/ray-project/kuberay/master/ray-operator/config/samples/pytorch-mnist/ray-job.pytorch-mnist.yaml`
- `kubectl -n ray apply -f ray-job.pytorch-mnist.yaml`
- `kubectl -n ray get pods`
- `kubectl -n ray get rayjob`
- `kubectl -n ray port-forward service/raycluster-kuberay-head-svc 8265:8265 > /dev/null &`