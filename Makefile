setup:
	python3 -m venv ~/.environment/Cloud-computing-project-image-analysis
	python3 -m source ~/.Cloud-computing-project-image-analysis/bin/activate

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C application.py

test:
	python -m pytest -vv test_application.py

