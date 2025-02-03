FROM python:3.10.0-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry && poetry config virtualenvs.create false

COPY rest_api_service/pyproject.toml rest_api_service/poetry.lock ./

RUN poetry install --no-root --only main

ENV PYTHONPATH=/app

COPY --chmod=777 rest_api_service/system/entrypoint.sh /usr/local/bin/entrypoint

COPY rest_api_service/src ./src

ENTRYPOINT ["entrypoint"]
