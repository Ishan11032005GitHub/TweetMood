# text_cleaner.py
from sklearn.base import BaseEstimator, TransformerMixin
import re

class TextClean(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return [self.clean_text(text) for text in X]

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"http\S+|www.\S+", "", text)  # Remove URLs
        text = re.sub(r"[^a-z\s]", "", text)         # Remove special chars
        text = re.sub(r"\s+", " ", text).strip()     # Remove extra spaces
        return text
