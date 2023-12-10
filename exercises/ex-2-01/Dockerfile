FROM python:3.10

WORKDIR /app
COPY ./log-output /app
RUN apt-get install -y curl
RUN pip3 install flask
CMD ["python", "app.py"]