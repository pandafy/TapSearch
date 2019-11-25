import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def lowerify(text):
    """
    Coverts all letters to lower cases.
    """
    return text.lower()

def docufy(text):
    """
    Returns different paragraph as list of different elements.
    """
    if len(text.split('\n\n')) == 1:
       return text.split('\r\n\r\n')
    else:
        return text.split('\n\n')

def cleanify(text):
    """
    Removes punctuations and stopping words.
    """
    tokens = word_tokenize(text)
    words = [word for word in tokens if word.isalpha()]
    return words

def indexify(text):
    text = cleanify(text)
    frequencies = { x : text.count(x) for x in text}
    return frequencies