Build image: `docker build -t mygenapp .`
My `k3d cluster create MYRANDOMGEN -a 3 --api-port localhost:6443`
Delete: `k3d cluster delete MYRANDOMGEN`
Create a deployment: `kubectl create deployment hashgenerator --image=mygenapp`
Import image to local cluster: `k3d image import -c MYRANDOMGEN mygenapp`