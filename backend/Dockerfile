FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app/backend/src


COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /usr/app
USER appuser

ENV PYTHONPATH=${PYTHONPATH}/usr/app/backend/src
ENV MY_PYTHON_PACKAGES=~/.local
ENV PATH $PATH:${MY_PYTHON_PACKAGES}/bin

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


EXPOSE 8000

CMD ["uvicorn", "web_app.http_api:app", "--reload", "--host", "0.0.0.0"]
