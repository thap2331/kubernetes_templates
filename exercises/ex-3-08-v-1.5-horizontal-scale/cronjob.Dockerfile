FROM python:3.10

WORKDIR /app
COPY ./todo-app/cronjob.py /app/cronjob.py
RUN pip3 install psycopg2
CMD ["python", "cronjob.py"]