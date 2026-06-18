import streamlit as st

from pdf_utils import extract_text
from summarizer import summarize_text
from keywords import extract_keywords
from report import create_report

st.set_page_config(page_title="Research Paper Analyzer")

st.title("📄 AI Research Paper Analyzer")

uploaded_file = st.file_uploader(
    "Upload Research Paper",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Analyzing Paper..."):

        text = extract_text(uploaded_file)

        summary = summarize_text(text)

        keywords = extract_keywords(text)

        report_path = create_report(
            summary,
            keywords
        )

    st.subheader("Summary")

    st.write(summary)

    st.subheader("Keywords")

    st.write(", ".join(keywords))

    with open(report_path, "rb") as f:

        st.download_button(
            "Download Report",
            f,
            file_name="analysis_report.pdf"
        )
