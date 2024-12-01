import pandas as pd
import pickle
import warnings
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os
import sys


def preprocess(text):
    stop_words = set(stopwords.words("english")) - {
        "not",
        "no",
        "couldn",
        "couldn't",
        "wouldn't",
        "shouldn't",
        "isn't",
        "aren't",
        "wasn't",
        "weren't",
        "don't",
        "doesn't",
        "hadn't",
        "hasn't",
        "won't",
        "can't",
        "mightn't",
        "needn't",
        "nor",
        "shouldn",
        "should've",
        "should",
        "weren",
        "wouldn",
        "mustn't",
        "mustn",
        "didn't",
        "didn",
        "doesn",
        "did",
        "does",
        "hadn",
        "hasn",
        "haven't",
        "haven",
        "needn",
        "shan't",
    }
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Tokenize text into words
    words = word_tokenize(text)
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    # Join the words back into a single string
    text = " ".join(words)
    return text


def process_sentence(sentence, vocab_dict):
    list1 = []
    for word in sentence.split():
        if word in vocab_dict:
            list1.append(vocab_dict[word])
        else:
            list1.append(vocab_dict["<UNK>"])
    return list1


def format_examples(data1, vocab_dict, maxlen):
    sequences_data = data1["cleaned_text"].apply(
        lambda sentence: process_sentence(sentence, vocab_dict)
    )
    padded_sequences_data = pad_sequences(sequences_data, padding="post", maxlen=100)
    return padded_sequences_data


def extractsuicidescore(text):
    # Determine the base path depending on the runtime environment
    if getattr(sys, 'frozen', False):  # Check if running in a PyInstaller bundle
        base_path = sys._MEIPASS  # PyInstaller extraction directory
    else:
        base_path = os.path.abspath(".")  # Directory of the current script

    # Resolve the full paths for the model and vocabulary files
    model_path = os.path.join(base_path, "data", "suicide_detection_model.pkl")
    vocab_path = os.path.join(base_path, "data", "vocab_dict.pkl")

    # Load the model and vocabulary files
    with open(model_path, "rb") as model_file:
        model_bistm_pretrained = pickle.load(model_file)
    with open(vocab_path, "rb") as vocab_file:
        vocab_dict = pickle.load(vocab_file)

    # Preprocess the input text
    cleanedtext = preprocess(text)

    # Prepare input data for prediction
    df = pd.DataFrame({"text": [text], "cleaned_text": [cleanedtext]})
    X_input = format_examples(df, vocab_dict, 100)

    # Run the prediction
    prediction = model_bistm_pretrained.predict(X_input, verbose=0).astype(float)

    return prediction.max()
