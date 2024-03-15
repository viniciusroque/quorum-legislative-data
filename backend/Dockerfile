FROM python:3.12-slim

WORKDIR /usr/app/src

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=${PYTHONPATH}/usr/app/backend/src