FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=5002

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential default-libmysqlclient-dev pkg-config \
      ca-certificates dumb-init \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5002

ENTRYPOINT ["dumb-init", "--"]
CMD ["gunicorn", "-w", "2", "-k", "gthread", "-b", "0.0.0.0:5002", "server:app"]