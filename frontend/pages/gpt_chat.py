import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="GPT Chat", page_icon="🤖", layout="wide")

st.title("🤖 GPT Chat Demo")


@st.cache_resource
def load_model():
    return pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")


try:
    generator = load_model()
except Exception as exc:
    st.error(f"Model loading failed: {exc}")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            result = generator(prompt, max_new_tokens=120, temperature=0.7, do_sample=True)
            response = result[0]["generated_text"]
            st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
