FROM python:3.12-alpine

# Zona horaria y usuario no-root
RUN apk add --no-cache tzdata && adduser -S -u 10001 app

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY cron_insert.py .

USER app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 TZ=America/Guatemala

ENTRYPOINT ["python", "/app/cron_insert.py"]