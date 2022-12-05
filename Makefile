install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py mylib/*.py

lint:
	pylint --disable=R,C main.py mylib/*.py

test:
	python -m pytest -vv --cov=mylib --cov=main test_*.py

all: install format lint