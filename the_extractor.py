import os
import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import glob

try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('punkt_tab')


class KeywordExtractor:
    def __init__(self, use_tfidf=False):
        self.stop_words = set(stopwords.words('english')).union({'hi', 'hello', 'hey', 'greetings'})

    def extract_frequency(self, messages, top_n=5):
        # Extract word based on the frequency.
        all_text = ' '.join(messages).lower()
        words = word_tokenize(all_text)
        words = [word for word in words if word.isalnum() and word not in self.stop_words and len(word) > 2]
        word_counts = Counter(words)
        return [word for word, count in word_counts.most_common(top_n)]

    def extract(self, messages, top_n=5, corpus=None):
        return self.extract_frequency(messages, top_n)
    
if __name__ == "__main__":
    print(word_tokenize.__module__)
