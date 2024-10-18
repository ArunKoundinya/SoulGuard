install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt

test:
		python -m pytest -vv test_main.py jupyternotebooks/test_*.py
		python -m pytest --nbval ./jupyternotebooks/tests_*.ipynb


format:
		black *.py

lint:
		pylint --disable=R,C main.py WebApp/*.py


all: install lint test format
