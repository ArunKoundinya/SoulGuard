import numpy as np
import pandas as pd
import pickle
import warnings
import nltk
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences


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

def process_sentence(sentence,vocab_dict):
  list1 = []
  for word in sentence.split():
    if word in vocab_dict:
      list1.append(vocab_dict[word])
    else:
      list1.append(vocab_dict["<UNK>"])
  return list1

def format_examples(data1, vocab_dict, maxlen):
  sequences_data = data1['cleaned_text'].apply(lambda sentence: process_sentence(sentence, vocab_dict))
  padded_sequences_data = pad_sequences(sequences_data,padding='post', maxlen=100)
  return padded_sequences_data


def extractsuicidescore(text):
    print("Input processed, running model...")
    print(text)
    model_bistm_pretrained = pickle.load(open("../data/suicide_detection_model.pkl", 'rb'))
    vocab_dict = pickle.load(open('../data/vocab_dict.pkl', 'rb'))
    
    cleanedtext = preprocess(text)
    
    df = pd.DataFrame({
    'text' : [text],
    'cleaned_text': [cleanedtext]
    })
    
    X_input = format_examples(df, vocab_dict, 100)
    
    prediction = model_bistm_pretrained.predict(X_input).astype(float)
    
    return prediction.max()

if  __name__ == "__main__":
    score = extractsuicidescore("I am Depressed")
    print(score)