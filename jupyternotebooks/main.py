import os
import sys
import re
import nltk
import string
import logging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import ssl
import nltk
import emoji  # Make sure to import the emoji module
ssl._create_default_https_context = ssl._create_unverified_context
logging.getLogger('nltk').setLevel(logging.WARNING)
sys.stdout = open(os.devnull, 'w')
sys.stdout = sys.__stdout__
from textblob import TextBlob
import sentimentmodel
import suicidemodel

def preprocess(text):
    stop_words = set(stopwords.words('english')) - { 'not', 'no', 'couldn', "couldn't", "wouldn't", "shouldn't", "isn't",
                                                "aren't", "wasn't", "weren't", "don't", "doesn't", "hadn't", "hasn't",
                                                 "won't", "can't", "mightn't","needn't","nor","shouldn","should've","should",
                                                 "weren","wouldn","mustn't","mustn","didn't","didn","doesn","did","does","hadn",
                                                 "hasn","haven't","haven","needn","shan't"}
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize text into words
    words = word_tokenize(text)
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    # Join the words back into a single string
    text = ' '.join(words)
    return text

predict_sentiment = sentimentmodel.hybrid_sentiment_analysis_worry("I am depressed")
print(predict_sentiment)
suicide_score = suicidemodel.extractsuicidescore("I am depressed")
print(suicide_score)