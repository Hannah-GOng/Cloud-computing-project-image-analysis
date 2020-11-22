setup:
		virtualenv --python $(which python3) ~/.Cloud-computing

install:
		pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
		pylint --disable=R,C application.py