docker build -t mygenapp .
k3d image import -c MYGEN mygenapp
kubectl apply -f ./manifests/