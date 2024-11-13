install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt

test:
		python -m pytest -vv jupyternotebooks/test_*.py

format:
		black *.py jupyternotebooks/*.py

lint:
		pylint --disable=R,C main.py WebApp/*.py


all: install lint test format
