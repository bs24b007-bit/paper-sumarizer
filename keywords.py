import re
from collections import Counter

STOPWORDS = {
    "the","a","an","and","or","is","are",
    "was","were","of","to","in","for",
    "on","with","by","as","at","that",
    "this","it","from","be","have","has"
}

def extract_keywords(text):

    words = re.findall(
        r'\w+',
        text.lower()
    )

    filtered = [
        word for word in words
        if word not in STOPWORDS
        and len(word) > 3
    ]

    freq = Counter(filtered)

    return [
        word
        for word,count
        in freq.most_common(15)
    ]
