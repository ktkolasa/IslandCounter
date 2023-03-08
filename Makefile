build:
	docker build --tag isl_counter .

run:
	docker run isl_counter

format:
	black src/*.py

lint:
	pylint src/*.py

test:
	pytest


all: build run format lint test