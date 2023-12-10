FROM python:3.10

WORKDIR /app
COPY ./log-reader /app
RUN pip3 install flask
CMD ["python", "app.py"]