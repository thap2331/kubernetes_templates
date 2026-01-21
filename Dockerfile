# kflow/Dockerfile
FROM python:3.9

# Install dependencies
RUN pip install pandas numpy scikit-learn

# Copy your entire kflow package
COPY . /app/kflow
WORKDIR /app

# Make it importable
ENV PYTHONPATH=/app