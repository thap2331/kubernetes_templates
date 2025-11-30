import kopf
import logging

@kopf.on.create('example.com', 'v1', 'greetings')
def on_create(spec, **kwargs):
    message = spec.get('message', 'Hello World')
    logging.info(f"Greeting created: {message}")
    print(f"Greeting: {message}")
