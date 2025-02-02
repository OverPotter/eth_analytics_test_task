black:
	black cron_service rest_api_service

isort:
	isort cron_service rest_api_service

ruff-check:
	ruff check cron_service rest_api_service

ruff-format:
	ruff check cron_service rest_api_service --fix

format: isort black ruff-format

up:
	docker compose up --remove-orphans --build \
		postgresql \
		cron_service \
		rest_api_service

db_downgrade:
	alembic downgrade -1

db_migrate:
	alembic revision --autogenerate -m "Upgrade database tables"

db_upgrade:
	alembic upgrade head
