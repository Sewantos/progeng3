SHELL := /bin/bash
POETRY := poetry
ALEMBIC := $(POETRY) run alembic
UVICORN := $(POETRY) run uvicorn

HOST ?= 0.0.0.0
PORT ?= 8000
ALEMBIC_INI := alembic.ini

.PHONY: test lint-all


lint-all:
	poetry run pre-commit run --all-files

test:
	poetry run pytest ./tests