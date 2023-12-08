# Exercise 1.12
## Prompt: Todo app with persisten volume
    -  Since the project looks really boring right now, let's add a picture! The goal is to add a daily image to the project. And every day a new image is fetched on the first request.

    - Get a random picture from Lorem Picsum like https://picsum.photos/1200 and display it in the project. 
        - Test: For test purposes save an image every 10 seconds.
        - Prod: Find a way to store the image so it stays the same for an entire day.

    - Make sure to cache the image into a volume so that the API isn't needed for new images every time we access the application or the container crashes.

    - Best way to test what happens when your container shuts down is likely by shutting down the container, so you can add logic for that as well, for testing purposes.

## Get started: Copy directory ex-1-08-v05 as ex-1-12-v06.

## Hint
- I do not understand this `Best way to test what happens when your container shuts down is likely by shutting down the container, so you can add logic for that as well, for testing purposes.` so I did not add test for this in my solution.

- Seperate the image-generator-app and todo-app to two different apps. You can either create two different pods or put both containers/apps in a pod. I am keeping both apps in one pod for now.

- I took a lot of inspiration from ex-1-10 and ex-1-11/

- I created one app that saves the image data to the folder. For testing purposes, it downloads and replaces existing image in persistent storage every 10 seconds.

- I updated the todo app so that the root page can show you the image.

## Test
    - If http://localhost:8081/ root page shows an image and todo app, then we know it works. Refresh after 10 seconds and view the updated image.

## Notes:
    - I do not understand instructions fully, so I updated the prompt to how I understand it.

## Solution
    - cd to this directory, run `make relaunch-cluster` and check http://localhost:8081/ and check again after 10 seconds to see the updated image.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-1/3-introduction-to-networking)</i>