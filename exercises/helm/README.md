# Install Helm (macOS)
brew install helm

# Install Helm (Linux)
helm version || curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Verify installation
helm version

# Add common repositories
helm repo add stable https://charts.helm.sh/stable
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo add kuberay https://ray-project.github.io/kuberay-helm/

# Update repositories
helm repo update

# Search for charts
helm search repo prometheus
helm search repo grafana


# Exercise 2: Your First Helm Deployment

## Make cluster
make cluster-dev

## Search for nginx
helm search repo nginx

## Install nginx
helm install my-nginx bitnami/nginx

## Check the release
helm list
kubectl get all

## Get values used
helm get values my-nginx

## See all default values
helm show values bitnami/nginx

## Upgrade with custom values
helm upgrade my-nginx bitnami/nginx --set replicaCount=3

## Rollback
helm rollback my-nginx 1

## Uninstall
helm uninstall my-nginx

# Exercise 3: Creating Your Own Helm Chart

# Create a new chart
helm create my-app

<!-- # This creates:
# my-app/
#   Chart.yaml          # Chart metadata
#   values.yaml         # Default configuration values
#   charts/             # Chart dependencies
#   templates/          # Kubernetes manifest templates
#     deployment.yaml
#     service.yaml
#     ingress.yaml
#     _helpers.tpl      # Template helpers -->