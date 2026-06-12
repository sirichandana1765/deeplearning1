import streamlit as st
from transformers import pipeline

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
    "<p class='sub-title'>English → Telugu & French Translation using Transformers</p>",
    unsafe_allow_html=True
)

@st.cache_resource
def load_models():
    en_fr = pipeline(
        "translation",
        model="facebook/nllb-200-distilled-600M"
    )

    en_te = pipeline(
        "translation",
        model="facebook/nllb-200-distilled-600M"
    )

    return en_fr, en_te


translator_fr, translator_te = load_models()

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

            if language == "French":
                result = translator_fr(
                    text,
                    src_lang="eng_Latn",
                    tgt_lang="fra_Latn"
                )

            else:
                result = translator_te(
                    text,
                    src_lang="eng_Latn",
                    tgt_lang="tel_Telu"
                )

            st.success("Translation Complete!")
            st.subheader("Output")
            st.write(result[0]["translation_text"])

    else:
        st.warning("Please enter text.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Powered by Transformers + Streamlit")
