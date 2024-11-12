import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import emoji  # Make sure to import the emoji module



# custom worrywords
Worry= pd.read_csv("../data/worrywords-v1.csv")
Worry = Worry[Worry['Mean']>0]
worrywords_dict = dict(zip(Worry['Term'],Worry['Mean']))

# custom words
custom_lexicon = {
    'suicide': -1.0, 'depression': -1.0, 'hurt': -0.8, 'pain': -0.8, 'loneliness': -0.8, 'struggle': -0.5, 'failure': -0.6, 'hope': 0.8, 'help': 0.7,
    'love': 0.9, 'support': 0.8, 'peace': 0.6, 'family': 0.7, 'friend': 0.8, 'happy': 1.0, 'life': 0.5, 'future': 0.5, 'escape': -0.4, 'numb': -0.6,
    'scared': -0.5, 'broken': -0.8, 'lost': -0.7, 'anxious': -0.5,
    'kill': -0.9, 'stop': -0.4, 'abuse': -0.9, 'guilty': -0.6, 'commit': -0.5, 'fake': -0.5, 'dead': -0.8, 'stress': -0.6, 'depress': -0.9, 'fail': -0.7,
    'death': -1.0, 'lose': -0.5, 'fear': -0.6, 'scar': -0.4, 'angry': -0.7, 'trauma': -0.8, 'cruel': -0.8, 'poison': -0.8, 'unlovable': -0.9,
    'lonely': -0.8, 'mistake': -0.5, 'destroy': -0.8, 'miserable': -0.9, 'mess': -0.4, 'die': -1.0, 'cry': -0.6, 'tear': -0.5, 'guilt': -0.6,
    'threat': -0.7, 'hopeless': -1.0, 'despair': -0.9, 'misery': -0.9, 'sorrow': -0.8, 'grief': -0.8, 'worthless': -0.9, 'anxiety': -0.7, 'upset': -0.5,
    'panic': -0.6, 'rage': -0.8, 'distress': -0.7, 'shattered': -0.9, 'inadequate': -0.7, 'rejected': -0.8, 'unloved': -0.9, 'cursed': -0.8,
    'burdened': -0.8, 'restless': -0.4, 'toxic': -0.8, 'suffer': -0.8, 'isolate': -0.7, 'discourage': -0.5, 'frighten': -0.6, 'struggling': -0.7,
    'manipulate': -0.5, 'cheat': -0.5, 'waste': -0.6, 'resent': -0.5, 'regret': -0.6, 'grudge': -0.6, 'detest': -0.7, 'void': -0.8, 'wreck': -0.7,
    'mourn': -0.8
}

#  custom emoji lexicon
emoji_lexicon = {'😂': 0.7, '😔': -0.5, '😏': 0.2, '😝': 0.6, '😘': 0.8, '❤': 0.9, '😳': 0.0, '😎': 0.6, '🥴': -0.3, '🙄': -0.1, '😭': -0.9,
                 '😬': -0.4, '🤭': 0.3, '😩': -0.6, '🤔': 0.0, '🥰': 0.9, '😀': 1.0, '🤗': 0.8, '😡': -0.8, '🤧': -0.6, '😐': 0.0,
                 '😁': 0.6, '😊': 0.7, '♥': 0.9, '😠': -0.7, '🥵': -0.5, '💜': 0.9, '💙': 0.8, '😈': -0.3, '💃': 0.5, '😍': 1.0,
                 '💕': 0.9, '🤯': -0.2, '🥳': 0.9, '😻': 1.0, '😤': -0.4, '🤣': 0.8, '😥': -0.7, '😖': -0.7, '🙂': 0.4, '😞': -0.8,
                 '😓': -0.6, '😪': -0.6}



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



# Function for calculating score for custom words
def calculation_custom_score(filter, customdict , text):
      words = word_tokenize(text.lower())
      scores = []

      for word in words:
        if word in customdict:
          scores.append(customdict[word])

      if scores:
        score = sum(scores) / len(scores)
        if filter == "worry":
          score = score / 3
          score = score * -1
        return score
      else :
        return 0

# Function to get TextBlob and VADER sentiment scores
def hybrid_sentiment_analysis_worry(text):
    
    vader_analyzer = SentimentIntensityAnalyzer()
    
    # TextBlob sentiment analysis
    blob = TextBlob(text)
    textblob_polarity = blob.sentiment.polarity  # Range from -1 (negative) to +1 (positive)

    # VADER sentiment analysis
    vader_scores = vader_analyzer.polarity_scores(text)
    vader_compound = vader_scores['compound']  # Range from -1 to +1
    # Custom lexicon scoring
    custom_score = calculation_custom_score("custom",custom_lexicon,text)

    # worrywords
    worry_score = calculation_custom_score("worry",worrywords_dict,text)

    # Emoji scoring
    emoji_score = calculation_custom_score("emoji",emoji_lexicon,text)

    # Combine scores with adjustable weights
    combined_score = (textblob_polarity * 0.10 + vader_compound * 0.50 +
                      custom_score * 0.10 + emoji_score * 0.10 + worry_score*0.20)

    # Scale the combined score to a 0 to 1 range
    scaled_score = (combined_score + 1) / 2

    return scaled_score

if  __name__ == "__main__":
    score = hybrid_sentiment_analysis_worry("I am Depressed")
    print(score)