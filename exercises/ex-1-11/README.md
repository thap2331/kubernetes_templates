# Exercise 1.11
## Prompt: Share persistent volume data between Log Output and ping pong
    - Let's share data between "Ping-pong" and "Log output" applications using persistent volumes. Create both a PersistentVolume and PersistentVolumeClaim and alter the Deployment to utilize it. As PersistentVolume is often maintained by cluster administrators rather than developers and are not application specific you should keep the definition for that separated.

    - Save the number of requests to "Ping-pong" application into a file in the volume and output it with the timestamp and hash when sending a request to our "Log output" application. In the end, the two pods should share a persistent volume between the two applications.

    - I am assuming we will have a two separate pods for each application.


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

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-1/4-introduction-to-storage)</i>