SHELL := /bin/bash

SERVER_NAME := webinator
SERVER_SOURCE = src
SERVER_APP := $(SERVER_SOURCE)/app.py
BUILD_TAG := latest

.PHONY: dev
dev: build
	sudo docker compose up -d server

.PHONY: build
build: $(SERVER_SOURCE)
	sudo docker build -t $(SERVER_NAME):$(BUILD_TAG) .

.PHONY: deps
deps: __pyenv__
	pip3 install -r requirements.txt

.PHONY: down
down:
	sudo docker compose down

.PHONY: lock-deps
lock-deps:
	pip3 freeze > requirements.txt

__pyenv__:
	python3 -m venv __pyenv__

.PHONY: admin
admin:
	sudo docker compose up -d admin
