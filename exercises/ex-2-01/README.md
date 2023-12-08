# Exercise 2.01: Connecting pods
## Prompt: Allow pods to talk to eachother
    - Connect the "Log output" application and "Ping-pong" application. Instead of sharing data via files use HTTP endpoints to respond with the number of pongs. Deprecate all the volume between the two applications for the time being.


## Get started: Copy directory ex-1-09 as ex-1-11.
## Hint
- I could not figure the way they set up in [devopswithkubernetes](https://devopswithkubernetes.com/part-1/4-introduction-to-storage). So I am going with persistent volume in a host machine inspired to this [blog](https://blog.ruanbekker.com/blog/2020/02/21/persistent-volumes-with-k3d-kubernetes/).
- Start by updating pong app that saves the data.
    - I added an endpoint `/pingpong`
- Update the log-output app.
    - Allow two lines, first the log output and second pong count.
    - I added an endping `/now`
- Add persistentvolume.yaml and persistentvolumeclaim.yaml
- Update pong app deployment yaml to incorporate persistent volume.
- Update log output app deployment yaml to incorporate persistent volume.
- Helpful commands
    - `kubectl get pv example-pv`
    - `kubectl get pvc file-claim`
- I made a significant changes from ex-1-09.

## Make sure both tests work
    - Start by testing pong app. This http://localhost:8081/pingpong should save data which will be useful in the next step.

    - Once we hit http://localhost:8081/now, we should see two lines, (a) log output and (b) second pong count. Go refresh http://localhost:8081/pingpong and come back here to ensure the pong count is updated.

## Notes:

## Solution
    - cd to this directory, run `make relaunch-cluster`. Check http://localhost:8081/pingpong, check http://localhost:8081/now, check http://localhost:8081/pingpong to see a new count, and finally check http://localhost:8081/now .

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-2/1-networking-between-pods)</i>