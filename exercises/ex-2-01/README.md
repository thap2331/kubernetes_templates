# Exercise 2.01: Connecting pods
## Prompt: Allow pods to talk to eachother
    - Connect the "Log output" application and "Ping-pong" application. Instead of sharing data via files use HTTP endpoints to respond with the number of pongs. Deprecate all the volume between the two applications for the time being.


## Get started: Copy directory ex-1-09 as ex-1-11.
## Hint
- Remove all volume references.
    - Remove pv and pvc files from manifests.
    - Remove volume references from deployments.

## Make sure both tests work
    - Start by testing pong app. This http://localhost:8081/pingpong should save data which will be useful in the next step.

    - Once we hit http://localhost:8081/now, we should see two lines, (a) log output and (b) second pong count. Go refresh http://localhost:8081/pingpong and come back here to ensure the pong count is updated.

## Notes:

## Solution
    - cd to this directory, run `make relaunch-cluster`. Check http://localhost:8081/pingpong, check http://localhost:8081/now, check http://localhost:8081/pingpong to see a new count, and finally check http://localhost:8081/now .

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-2/1-networking-between-pods)</i>