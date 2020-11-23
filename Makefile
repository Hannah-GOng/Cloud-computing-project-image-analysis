setup:
	python3 -m venv ~/.virt

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	pylint --disable=R,C application.py

all: setup install test