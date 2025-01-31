black:
	black src

isort:
	isort src

ruff-check:
	ruff check src

ruff-format:
	ruff check src --fix

format: isort black ruff-format

up:
	docker compose up --remove-orphans --build \
		backend \
		postgresql

db_downgrade:
	alembic downgrade -1

db_migrate:
	alembic revision --autogenerate -m "Upgrade database tables"

db_upgrade:
	alembic upgrade head
