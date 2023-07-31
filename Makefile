PROJECT_SOURCE := src

.PHONY: run
run: deps
	flask --app $(PROJECT_SOURCE)/app run

.PHONY: deps
deps: set-env
	pip3 install -r requirements.txt

.PHONY: set-env
set-env:
	python3 -m venv __pyenv__
