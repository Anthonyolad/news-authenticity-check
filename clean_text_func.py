# Import necessary library
import re
import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Set stopwords
stop_words = set(stopwords.words("english"))

# Create the fuction to clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z]", " ", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)
