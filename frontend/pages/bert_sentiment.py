import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="BERT Sentiment", page_icon="🧠", layout="wide")

st.title("🧠 BERT Sentiment Demo")


@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


try:
    classifier = load_model()
except Exception as exc:
    st.error(f"Model loading failed: {exc}")
    st.stop()

text = st.text_area("Enter text to analyze")

if st.button("Analyze") and text:
    result = classifier(text)
    st.write(result[0])
