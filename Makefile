setup:
	python3 -m venv ~/.virt

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	python -m unittest discover -s ./

all: setup install lint