FROM python:3.10

WORKDIR /app
COPY ./todo-app /app
RUN pip3 install flask psycopg2
CMD ["python", "app.py"]