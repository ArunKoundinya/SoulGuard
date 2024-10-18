import pandas as pd

data = pd.read_csv("data/SoulG_Update.csv", nrows=20)


def test_cleaned_text():
    assert len(data["text"][0]) > data["wordlength"][0]


def test_lemmatized():
    for word in data["cleaned_text"][0].split():
        assert not word.endswith("ing"), f"Found a word ending with 'ing': {word}"


def test_lowercase():
    for word in data["cleaned_text"][0].split():
        assert word.islower()

