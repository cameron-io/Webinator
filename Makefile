PROJECT := webinator
BUILD_TAG := latest
SOURCE := src
NETWORK := devNET

.PHONY: dev
dev: build deps env
	sudo docker run -dp 5000:5000 $(PROJECT):$(BUILD_TAG) --name $(PROJECT) --network $(NETWORK)

.PHONY: build
build: $(SOURCE)
	sudo docker build -t $(PROJECT):$(BUILD_TAG) .

.PHONY: env
env: .env
	sudo docker compose up -d

.PHONY: deps
deps: __pyenv__
	pip3 install -r requirements.txt

.PHONY: set-deps
set-deps:
	pip3 freeze > requirements.txt

__pyenv__:
	python3 -m venv __pyenv__
