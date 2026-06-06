# preprocessing.py

import re
import nltk
from nltk.tokenize import (
    sent_tokenize,
    word_tokenize
)

# -----------------------------------
# Download NLTK resources only if missing
# -----------------------------------
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')


def clean_text(text):
    """
    Cleans input text.

    Steps:
    - Convert to lowercase
    - Remove punctuation
    - Remove extra spaces
    """

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(
        r"[^\w\s]",
        "",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

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