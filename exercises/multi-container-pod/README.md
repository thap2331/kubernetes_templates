
# Tasks
### Apply this pod and observe both containers
For a multi-container pod, you need to specify which container you want to exec into using the -c or --container flag.

`kubectl exec -it multi-container-pod -c app -- /bin/bash`

`kubectl exec -it multi-container-pod -c log-sidecar -- /bin/sh`
### Exec into the nginx container and generate some traffic
- Gen logs
    - `kubectl exec multi-container-pod -c app -- curl -s localhost`

### Check the sidecar logs: kubectl logs multi-container-pod -c log-sidecar
- `kubectl logs multi-container-pod -c log-sidecar`
### Modify to add a third container that counts log lines

- `kubectl delete pod multi-container-pod`
- `kubectl apply -f deployment2.yaml`
- `kubectl exec multi-container-pod -c app -- curl -s localhost`
- `kubectl exec multi-container-pod -c app -- curl -s localhost/abc`
- `k logs multi-container-pod -c log-counter`

