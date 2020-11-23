setup:
	python3 -m venv ~/.environment/Cloud-computing-project-image-analysis

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C application.py

test:
	python -m pytest -vv test_application.py

