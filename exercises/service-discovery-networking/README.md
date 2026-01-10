# Networking Deep Dive
## Understanding Services
- Kubernetes Services provide stable endpoints for pods:

   - ClusterIP: Internal cluster access (default)
   - NodePort: Exposes on each node's IP at a static port
   - LoadBalancer: Cloud provider load balancer
   - ExternalName: DNS CNAME record

## Exercise: Service Discovery
- Objective: Understand how pods communicate through services.


### Deploy the above resources
`make deploy`
### Create a test pod: kubectl run test --image=busybox -it --rm -- sh
`kubectl -n network-ns run test --image=busybox -it --rm -- sh`
`kubectl -n network-ns get service backend-service`
### Inside the test pod, try: wget -O- backend-service
`wget -O- backend-service`
### Check DNS: nslookup backend-service
`nslookup backend-service`
### Try the fully qualified domain name that came from above.
`wget -O- backend-service.network-ns.svc.cluster.local`

### Scale the deployment and observe service load balancing
- First, let's create and apply the deployment and service:
- `kubectl -n network-ns apply -f deployment2.yaml`

- On one terminal,
   - `kubectl -n network-ns get pods -l app=backend -w`

- Another terminal, Test load balancing - # Run multiple requests and see different pods responding
    - You should see responses from different pods!
   ```
        kubectl -n network-ns run test --image=busybox -it --rm -- sh -c "
        for i in 1 2 3 4 5 6 7 8 9 10; do
        echo 'Request #'\$i:
        wget -qO- backend-service
        echo
        echo '---'
        done
        "

   ```

- Notes
    - Rollout if needed
        - `kubectl -n network-ns rollout status deployment backend`

### Create a frontend deployment with label app: frontend
- `kubectl -n network-ns apply -f frontend.yaml`
- `kubectl -n network-ns get pods -l app=frontend`
- `kubectl -n network-ns get pods -l app=backend`
- `kubectl -n network-ns get service backend-service`
### Apply the network policy
- Test Connectivity BEFORE Applying Network Policy
- Important: Test that everything works first, then apply the policy to see the difference.
-  Test from frontend pod (should work)
`FRONTEND_POD=$(kubectl -n network-ns get pod -l app=frontend -o jsonpath='{.items[0].metadata.name}')`
`echo $FRONTEND_POD`
- Test from a random pod (should also work before policy)
`kubectl -n network-ns exec $FRONTEND_POD -- wget -qO- --timeout=2 backend-service`
### Test connectivity from frontend pods (should work)
- `kubectl -n network-ns apply -f network.yaml`
- `kubectl -n network-ns get networkpolicy`
- `kubectl -n network-ns describe networkpolicy backend-policy`
- ```
        # Test from frontend - this SHOULD WORK
        echo "Testing from frontend pod (should succeed):"
        kubectl -n network-ns exec $FRONTEND_POD -- wget -qO- --timeout=2 backend-service

        # Try multiple times to confirm
        echo -e "\nMultiple requests from frontend:"
        kubectl -n network-ns exec $FRONTEND_POD -- sh -c '
        for i in 1 2 3; do
        echo "Request #$i:"
        wget -qO- --timeout=2 backend-service 2>&1 | head -1
        done'

    ```
### Test from other pods (should fail)
`kubectl  -n network-ns run unauthorized-pod --image=busybox --rm -i -- wget -qO- --timeout=2 backend-service`