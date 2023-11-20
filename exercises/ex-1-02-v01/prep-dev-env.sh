docker build -t mygenapp .
k3d image import -c TODOV01 mygenapp
kubectl apply -f deployment.yaml