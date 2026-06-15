import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

st.set_page_config(
    page_title="AI Translator",
    page_icon="🌍",
    layout="wide"
)

# Background Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e3a8a 50%,
        #3b82f6 100%
    );
}

.main-title {
    text-align: center;
    color: white;
    font-size: 3rem;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #dbeafe;
    font-size: 1.2rem;
    margin-bottom: 25px;
}

.box {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 class='main-title'>🌍 AI Translator</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>English → Telugu & French Translation using NLLB</p>",
    unsafe_allow_html=True
)

MODEL_NAME = "facebook/nllb-200-distilled-600M"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()

def translate_text(text, target_lang):
    tokenizer.src_lang = "eng_Latn"

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    generated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(target_lang),
        max_length=512
    )

    translated_text = tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True
    )[0]

    return translated_text

st.markdown("<div class='box'>", unsafe_allow_html=True)

language = st.selectbox(
    "Select Target Language",
    ["French", "Telugu"]
)

text = st.text_area(
    "Enter English Text",
    height=150
)

if st.button("Translate"):

    if text.strip():

        with st.spinner("Translating..."):

            try:
                if language == "French":
                    target_lang = "fra_Latn"
                else:
                    target_lang = "tel_Telu"

                translated = translate_text(text, target_lang)

                st.success("Translation Complete!")
                st.subheader("Output")
                st.write(translated)

            except Exception as e:
                st.error(f"Translation failed: {e}")

    else:
        st.warning("Please enter text.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Powered by Hugging Face Transformers + Streamlit")
