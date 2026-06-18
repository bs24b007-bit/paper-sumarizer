# summarizer.py

from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text):

    text = text[:3000]

    summary = summarizer(
        text,
        max_length=200,
        min_length=50,
        do_sample=False
    )

    return summary[0]["summary_text"]