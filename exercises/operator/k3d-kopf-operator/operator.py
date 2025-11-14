import kopf
import logging

@kopf.on.create('example.com', 'v1', 'greetings')
def on_create(spec, **kwargs):
    message = spec.get('message', 'Hello from Kopf Operator!')
    logging.info(f"Greeting received: {message}")
