FROM python:3.10.0-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    cron \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry && poetry config virtualenvs.create false

COPY cron_service/pyproject.toml cron_service/poetry.lock ./

RUN poetry install --no-root --only main

ENV PYTHONPATH=/app

COPY cron_service/src ./src
COPY cron_service/alembic.ini ./alembic.ini

COPY --chmod=644 cron_service/system/crontab /etc/cron.d/crontab
COPY --chmod=777 cron_service/system/entrypoint.sh /usr/local/bin/entrypoint

RUN crontab /etc/cron.d/crontab

ENTRYPOINT ["entrypoint"]
