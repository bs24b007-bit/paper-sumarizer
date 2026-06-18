import re
from collections import Counter

STOPWORDS = {
    "the","a","an","and","or","is","are",
    "was","were","of","to","in","for",
    "on","with","by","as","at","that",
    "this","it","from","be","have","has"
}

def summarize_text(text):

    sentences = re.split(r'(?<=[.!?]) +', text)

    words = re.findall(r'\w+', text.lower())

    words = [
        w for w in words
        if w not in STOPWORDS
    ]

    freq = Counter(words)

    sentence_scores = {}

    for sentence in sentences:

        score = 0

        for word in re.findall(
            r'\w+',
            sentence.lower()
        ):

            score += freq.get(word,0)

        sentence_scores[sentence] = score

    ranked = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )

    summary = " ".join(ranked[:5])

    return summary
