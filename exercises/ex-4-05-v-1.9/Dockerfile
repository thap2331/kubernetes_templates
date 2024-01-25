FROM python:3.10

WORKDIR /app
RUN pip3 install flask psycopg2
COPY ./todo-app /app
CMD ["python", "app.py"]