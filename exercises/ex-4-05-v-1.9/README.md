# Exercise 4-05

## Prompt - Add done

## Prereqs

## Hint
- Get started: Copy directory ex-4-02-v-1.7-probes as ex-4-05-v-1.9
- Add `@app.route('/todos/<int:task_id>', methods=['PUT'])`
- Update create table in postgres manifest
    - `sleep 3 && psql -U $POSTGRES_USER -d $POSTGRES_DB -c 'CREATE TABLE IF NOT EXISTS todotable (id SERIAL PRIMARY KEY, title VARCHAR(50), description VARCHAR(140), done VARCHAR(4));`

## Test

## Solution
- cd to this directory, run `make relaunch-cluster`.
- All shoudl work.

<i>Source: [DevOps with Kubernetes](https://devopswithkubernetes.com/part-4/1-update-strategies-and-prometheus)</i>