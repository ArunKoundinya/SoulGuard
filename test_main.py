import jupyternotebooks.mainpredictions


def test_score():
    assert "Three" == jupyternotebooks.mainpredictions.finalpredictions("I am Depressed")
