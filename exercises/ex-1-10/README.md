# Exercise 1.10
## Prompt: Share simple ephemeral volume across pods
    -  "Log output" application currently outputs a timestamp and a random string to the logs.
    - Split the "Log output" application into two different containers within a single pod:
        - One generates a new timestamp every 5 seconds and saves it into a file.
        - The other reads that file and outputs it with a hash for the user to see.
    - Either application can generate the hash. The reader or the writer.

## Get started: Copy directory ex-1-09 as ex-1-10.
## Hint
- Create two apps.
- Update `deployment.yaml` by adding volumes, containers, and others as needed.

## Test
    - If http://localhost:8081/show works, then we know it works. If you refresh and it should give you new timestamp.

## Notes:

## Solution
    - cd to this directory, run `make relaunch-cluster` and check http://localhost:8081/show.

<i>Source: [DevOps with Kubernetes; part 1- introduction to storage](https://devopswithkubernetes.com/part-1/4-introduction-to-storage)</i>