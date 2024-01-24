FROM python:3.10

WORKDIR /app
COPY ./todo-app /app
RUN pip3 install schedule requests
CMD ["python", "image-generator.py"]