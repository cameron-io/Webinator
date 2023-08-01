PROJECT_SOURCE := src

.PHONY: run
run: deps
	flask --app $(PROJECT_SOURCE)/app run

.PHONY: db
db: .env
	sudo docker compose up -d db

.PHONY: deps
deps: __pyenv__
	pip3 install -r requirements.txt

.PHONY: set-deps
set-deps:
	pip3 freeze > requirements.txt

__pyenv__:
	python3 -m venv __pyenv__
