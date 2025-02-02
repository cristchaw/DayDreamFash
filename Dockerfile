FROM --platform=$TARGETPLATFORM python:3.13.0-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=core.settings
ENV SECRET_KEY=temporary-secret-key-for-collectstatic
ENV DEBUG=False
ENV DATABASE_URL=sqlite:///db/db.sqlite3

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/db && \
    python manage.py collectstatic --noinput

EXPOSE ${PORT} 
