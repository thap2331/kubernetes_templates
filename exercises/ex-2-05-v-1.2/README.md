# Exercise 2.05: Secrets
## Prompt
- Pass secrets using secret.yaml
- Note: I am not going with SOPS for now because I will use secrets manager on the cloud.

## Prereqs
- NA

## Get started: Copy directory ex-2-04-v-1.1 as ex-2-05-v-1.2

## Hint
- Convert a string to base64 and use this in secret.yaml that you will create next.
- Create a secret.yaml file in manifests.
    - Choose a password and convert to base64: `echo 'password' | base64`
    - Use this as a secret in secret.yaml
- Add secrets to a container in deployment.
- Add a mechanism in your app so that you can view the password. I added a logging functionality.
- Use `kubectl create namespace todotest`

## Test
    - Go to your endpoint where it logs your password. See the logs in your app and confirm your password.

## Notes:
- To add a defualt namespace, you have to manually add `kubectl config set-context --current --namespace=todotest`

## Solution
    - cd to this directory, run `make relaunch-cluster` and check http://localhost:8081/ and See the logs in your app and confirm your secret as `password`.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-2/3-configuring-applications)</i>