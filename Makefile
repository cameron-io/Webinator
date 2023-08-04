SHELL := /bin/bash
PROJECT=webinator
BUILD_TAG=latest

SOURCE := src

.PHONY: dev
dev: build deps env
	sudo docker compose up -d

.PHONY: build
build: $(SOURCE) env
	sudo docker build -t $(PROJECT):$(BUILD_TAG) .

.PHONY: env
env: .env
	source .env

.PHONY: deps
deps: __pyenv__
	pip3 install -r requirements.txt

.PHONY: down
down:
	sudo docker compose down

.PHONY: set-deps
set-deps:
	pip3 freeze > requirements.txt

__pyenv__:
	python3 -m venv __pyenv__
