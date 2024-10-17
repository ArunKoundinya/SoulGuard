install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt
		python -m nltk.downloader wordnet
		python -m nltk.downloader punkt
		python -m nltk.downloader stopwords


test:
		python -m pytest -vv test_main.py
		python -m pytest --nbval ./jupyternotebooks/*.ipynb


format:
		black *.py

lint:
		pylint --disable=R,C main.py WebApp/*.py


all: install lint test format
