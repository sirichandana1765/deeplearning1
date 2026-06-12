import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="🌍 AI Translator",
    page_icon="🌍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e3a8a, #2563eb);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #dbeafe;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='main-title'>🌍 AI Language Translator</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Translate English to Telugu or French using Transformers</div>",
    unsafe_allow_html=True
)

# Load models
@st.cache_resource
def load_models():
    en_te = pipeline(
        "translation",
        model="Helsinki-NLP/opus-mt-en-mul"
    )

    en_fr = pipeline(
        "translation",
        model="Helsinki-NLP/opus-mt-en-fr"
    )

    return en_te, en_fr


translator_te, translator_fr = load_models()

st.markdown("<div class='card'>", unsafe_allow_html=True)

language = st.selectbox(
    "Select Target Language",
    ["Telugu", "French"]
)

text = st.text_area(
    "Enter English Text",
    height=150,
    placeholder="Type your English sentence here..."
)

if st.button("🚀 Translate", use_container_width=True):

    if text.strip():

        with st.spinner("Translating..."):

            if language == "Telugu":
                result = translator_te(text)[0]["translation_text"]
            else:
                result = translator_fr(text)[0]["translation_text"]

        st.success("Translation Complete!")

        st.subheader("Translated Text")
        st.write(result)

    else:
        st.warning("Please enter some text.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Built with Streamlit + Hugging Face Transformers 🤖")
