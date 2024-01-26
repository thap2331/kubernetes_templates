FROM python:3.10

WORKDIR /app
RUN pip3 install psycopg2
COPY ./todo-app/cronjob.py /app/cronjob.py
CMD ["python", "cronjob.py"]