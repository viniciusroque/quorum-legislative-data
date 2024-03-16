FROM python:3.12-slim

WORKDIR /usr/app/backend/src/web_app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=${PYTHONPATH}/usr/app/backend/src