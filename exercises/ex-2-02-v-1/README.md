# Exercise 2.02
## Prompt
- Create a new container for the backend of the todo application.

- You can use graphql or other solutions if you want.

- Use ingress routing to enable access to the backend.

- Create a POST /todos endpoint and a GET /todos endpoint in the new service where we can post a new todo and get all of the todos. You can also move the image logic to the new service if it requires backend logic.

- The todos can be saved into memory, we'll add database later.

- Frontend already has an input field. Connect it into our backend so that inputting data and pressing send will add a new todo into the list.

## Get started: Copy directory ex-1-13-v07 as ex-2-02-v01.

## Hint
- I am not solving this problem, because I do not understand the when it says "graphql or other solutions if you want" as a backend contaioner.

## Test
    - If http://localhost:8081/ root page shows an image and todo app, then we know it works. Refresh after 10 seconds and view the updated image.

## Notes:

## Solution
    - cd to this directory, run `make relaunch-cluster` and check http://localhost:8081/ and check again after 10 seconds to see the updated image.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-1/4-introduction-to-storage)</i>