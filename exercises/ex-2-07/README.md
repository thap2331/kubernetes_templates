# Exercise 2.06: Documentation and ConfigMaps
## Prompt: Add ConfigMaps
    - Use the official Kubernetes documentation for this exercise. https://kubernetes.io/docs/concepts/configuration/configmap/ and https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/ should contain everything you need.

    - Create a ConfigMap for a "dotenv file". A file where you define environment variables that are loaded by the application. For this use an environment variable "MESSAGE" with value "Hello" to test and print the value. The values from ConfigMap can be either saved to a file and read by the application, or set as environment variables and used by the application through that.

## Get started: Copy directory ex-2-03 as ex-2-06.
## Hint
- Update app to retrieve `MESSAGE` variable from environment.
- Add `envFrom` in spec of a container in your deployment.
- (This is the way I did it): Create a `.env` file.
- Add `kubectl` command to create a configmap after creating a cluster: `kubectl create configmap newconfig --from-env-file=.env --namespace=logtest`

## Tests
    - This http://localhost:8081/pingpong should show your `MESSAGE` environment variable.

## Notes:

## Solution
    - cd to this directory, run `make relaunch-cluster`. It should show your `MESSAGE` environment variable as configured in the app.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-2/4-statefulsets-and-jobs)</i>