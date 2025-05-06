.PHONY: init, check
init:
	alembic init migrations

check:
	black .
	isort .
	flake8 .