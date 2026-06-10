import streamlit as st
from transformers import pipeline

st.title("BERT Sentiment Analysis")

@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

classifier = load_model()

text = st.text_area("Enter text")

if st.button("Analyze"):
    if text:
        result = classifier(text)
        st.write(result[0])