# DevOps with Kubernetes

## Part 1

Link: <https://devopswithkubernetes.com/part-1>

Contents:

1. First Deploy
2. Introduction to Debugging
3. Introduction to Networking
4. Introduction to Storage
5. Summary

Exercises:

- Exercise 1.01: Getting started ([NA]())
- Exercise 1.02: Project v0.1 ([NA]())
- Exercise 1.03: Declarative approach ([NA]())
- Exercise 1.04: Project v0.2 ([NA]())
- Exercise 1.05: Project v0.3 ([link](./exercises/ex-1-05-v03/README.md))
- Exercise 1.06: Project v0.4; Simple networking with NodePort ([link](./exercises/ex-1-06-v04/README.md))
- Exercise 1.07: External access with Ingress ([link](./exercises/ex-1-07/README.md))
- Exercise 1.08: Project v0.5 ([link](./exercises/ex-1-08-v05/README.md))
- Exercise 1.09: More services ([link](./exercises/ex-1-09/README.md))
- Exercise 1.10: Even more services ([link](./exercises/ex-1-10/README.md))
- Exercise 1.11: Persisting data ([link](./exercises/ex-1-11/README.md))
- Exercise 1.12: Project v0.6 ([link](./exercises/ex-1-12-v06/README.md))
- Exercise 1.13: Project v0.7 ([link](./exercises/ex-1-13-v07/README.md))

## Part 2

Link: <https://devopswithkubernetes.com/part-2>

Contents:

1. Networking between pods
2. Organizing a cluster
3. Configuring applications
4. Statefulsets and Jobs
5. Monitoring
6. Summary

Exercises:

- Exercise 2.01: Connecting pods ([link](./exercises/ex-2-01/README.md))
- Exercise 2.02: Project v1.0 ([link](./exercises/ex-2-02-v-1/README.md))
- Exercise 2.03: Keep them separated ([link](./exercises/ex-2-03/README.md))
- Exercise 2.04: Project v1.1 ([link](./exercises/ex-2-04-v-1.1/README.md))
- Exercise 2.05: Secrets ([link](./exercises/ex-2-05-v-1.2/README.md))
- Exercise 2.06: Documentation and ConfigMaps ([link](./exercises/ex-2-06/README.md))
- Exercise 2.07: Stateful applications ([link](./exercises/ex-2-07/README.md))
- Exercise 2.08: Project v1.2 ([link](./exercises/ex-2-08-v-1.2/README.md))
- Exercise 2.09: Daily todos ([link](./exercises/ex-2-09/README.md))
- Exercise 2.10: Project v1.3 ([link](./exercises/ex-2-10-v-1.3-monitoring/README.md))

## Part 3

Link: <https://devopswithkubernetes.com/part-3>

Contents:

1. Introduction to Google Kubernetes Engine
2. Deployment Pipeline
3. GKE features
4. Summary

Exercises:

- Exercise 3.01: Pingpong GKE ([link](./exercises/ex-3-01-Pingpong-GKE/README.md))
- Exercise 3.02: Back to Ingress ([link](./exercises/ex-3-02-Pingpong-GKE-Ingress/README.md))
- Exercise 3.03: Project v1.4 ([link](./exercises/ex-3-03-Pingpong-GKE-GitHub-Actions/README.md))
- Exercise 3.04: Project v1.4.1 ([link](./exercises/ex-3-04-Pingpong-GKE-GActions-each-branch/README.md))
- Exercise 3.05: Project v1.4.2 ([link](./exercises/ex-3-05-Pingpong-GKE-GActions-delete-branch/README.md))
- Exercise 3.06: DBaaS vs DIY ([skipping]())
- Exercise 3.07: Commitment ([skipping]())
- Exercise 3.08: Project v1.5 ([link]())
- Exercise 3.09: Sensible processes ([skipping]())
- Exercise 3.10: Project v1.6 ([skipping]())

## Part 4

Link: <https://devopswithkubernetes.com/part-4>

Contents:

1. Update Strategies and Prometheus
2. Messaging Systems
3. GitOps
4. Summary

Exercises:

- Exercise 4.01: Readiness Probe ([link]())
- Exercise 4.02: Project v1.7 ([link]())
- Exercise 4.03: Prometheus ([link]())
- Exercise 4.04: Project v1.8 ([link]())
- Exercise 4.05: Project v1.9 ([link]())
- Exercise 4.06: Project v2.0 ([link]())
- Exercise 4.07: GitOpsify Cluster ([link]())
- Exercise 4.08: Project v2.1 ([link]())

## Part 5

Link: <https://devopswithkubernetes.com/part-5>

Contents:

1. Kubernetes Internals
2. Custom Resource Definitions
3. Service Mesh
4. Beyond Kubernetes
5. Summary and end

Exercises:

- Exercise 5.01: DIY CRD & Controller ([link]())
- Exercise 5.02: Project: Service Mesh Edition ([link]())
- Exercise 5.03: Learn from external material ([link]())
- Exercise 5.04: Platform comparison ([link]())
- Exercise 5.05: Deploy to Serverless ([link]())
- Exercise 5.06: Landscape ([link]())

# Networking
- Exercise 1.06: Project v0.4; Simple networking with NodePort ([link](./exercises/ex-1-06-v04/README.md))

# Set up
1. [k3d](https://k3d.io/v5.6.0/#installation)
2. kubectl
    - [In Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-using-native-package-management)
3. Able to run `make` command
    ```sh 
        sudo apt-get update
        sudo apt-get -y install make
    ```
4. Cluseter-monitoring
    - You can use whatever you like. I do like [k9s](https://webinstall.dev/k9s/)