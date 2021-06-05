import re
import string
import nltk
from nltk.corpus import stopwords


EMBED_SIZE = 100
MAX_FEATURES = 50000
MAX_LEN = 2000

def build_stopwordlist():
    return stopwords.words('english').append('subject:')

def cleanEmail(emailText, wordlist):
    lower = emailText.lower()
    removeStop = ' '.join([word for word in lower.split() if word not in wordlist])
    removeUrl = re.sub(r"http\S+", "", removeStop)
    removePunc = removeUrl.translate(str.maketrans(dict.fromkeys(string.punctuation)))
    return removePunc

