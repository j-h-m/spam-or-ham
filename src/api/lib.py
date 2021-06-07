import re
import string
import json
import pickle
import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)


EMBED_SIZE = 100
MAX_FEATURES = 50000
MAX_LEN = 2000

def _unpickle_stopwords(path):
    with open(path, "rb") as fp:
       b = pickle.load(fp)
    return b

def _load_tokenizer(path):
    with open(path) as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    return tokenizer

def _cleanEmail(emailText, stopwords):
    lower = emailText.lower()
    removeStop = ' '.join([word for word in lower.split() if word not in stopwords])
    removeUrl = re.sub(r"http\S+", "", removeStop)
    removePunc = removeUrl.translate(str.maketrans(dict.fromkeys(string.punctuation)))
    return removePunc

def preprocess(emailText, tokenizer, stopwords):
    cleaned = _cleanEmail(emailText, stopwords)
    arr = np.array(tokenizer.texts_to_sequences([cleaned]), dtype=object)
    padding = pad_sequences(arr, maxlen=MAX_LEN)
    return padding

class Predictor:
    def __init__(self, modelPath, stopwordsPath, tokenizerPath):
        self.model = keras.models.load_model(modelPath)
        self.stopwords = _unpickle_stopwords(stopwordsPath)
        self.tokenizer = _load_tokenizer(tokenizerPath)
    
    def computePrediction(self, emailText):
        preprocessedText = preprocess(emailText, tokenizer=self.tokenizer, stopwords=self.stopwords)
        result = self.model.predict(preprocessedText)
        try:
            result = round(result[0][0], 2)
        except:
            print('failed to extract result from result list')

        return result