install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt

test:
		python -m pytest -vv jupyternotebooks/test_*.py

format:
		black *.py jupyternotebooks/*.py

lint:
		pylint --disable=R,C,E0401,E0611,W0212,W1514,W0611,W0212,W0622,W0613,W0212,W0611,W1510 main.py WebApp/*.py jupyternotebooks/*.py


all: install lint test format
