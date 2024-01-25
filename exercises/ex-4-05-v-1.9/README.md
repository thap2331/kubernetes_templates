# Exercise 4-05

## Prompt - Add done field

## Hint
- Get started: Copy directory ex-4-02-v-1.7-probes as ex-4-05-v-1.9
- Update create table in postgres manifest
    - `sleep 3 && psql -U $POSTGRES_USER -d $POSTGRES_DB -c 'CREATE TABLE IF NOT EXISTS todotable (id SERIAL PRIMARY KEY, title VARCHAR(50), description VARCHAR(140), done VARCHAR(4));`
- Add `@app.route('/todos/<int:task_id>', methods=['PUT'])`
    - Make other necessary changes
- Update app to allow edit the done (optional)
- PUT request: `curl -X PUT -H "Content-Type: application/json" -d '{"key1":"value"}' http://172.19.0.2/todos/1`

## Test

## Solution
- cd to this directory, run `make relaunch-cluster`.
- Get ingress using `kubectl get ing -n todotest`
- Make a PUT request using `curl -X PUT -H "Content-Type: application/json" -d '{"key1":"value"}' http://172.19.0.2/todos/1`

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-4/1-update-strategies-and-prometheus)</i>