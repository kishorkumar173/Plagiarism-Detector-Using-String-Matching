# preprocessing.py

import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download tokenizer once
nltk.download("punkt")


def clean_text(text):
    """
    Cleans input text.

    Steps:
    - convert to lowercase
    - remove punctuation
    - remove extra spaces
    """

    # lowercase
    text = text.lower()

    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def sentence_tokenization(text):
    """
    Splits text into sentences.
    """ 

    return sent_tokenize(text)


def word_tokenization(text):
    """
    Splits text into words.
    """

    return word_tokenize(text)