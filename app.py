import streamlit as st

from pdf_utils import extract_text
from summarizer import summarize_text
from keywords import extract_keywords
from report import create_report

st.title("AI Research Paper Analyzer")

uploaded_file = st.file_uploader(
    "Upload Research Paper",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Analyzing..."):

        text = extract_text(uploaded_file)

        summary = summarize_text(text)

        keywords = extract_keywords(text)

        st.subheader("Summary")

        st.write(summary)

        st.subheader("Keywords")

        st.write(keywords)

        report = create_report(
            summary,
            keywords
        )

        with open(report, "rb") as f:

            st.download_button(
                "Download Report",
                f,
                file_name="analysis_report.pdf"
            )