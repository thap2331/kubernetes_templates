## Install minikube (in Linux) 
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

- See here for mac or windows
- https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download


#### If need to scale down proxy-agent
kubectl scale deployment proxy-agent -n kubeflow --replicas=0