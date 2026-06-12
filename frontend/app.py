import streamlit as st

st.set_page_config(
    page_title="Deep Learning 1 Frontend",
    page_icon="🚀",
    layout="wide",
)

st.title("Deep Learning 1 Streamlit Frontend")
st.write("Choose a demo to run from the sidebar navigation.")

st.info("Run this app with: streamlit run frontend/app.py")

st.subheader("Available demos")
st.markdown("- 🤖 GPT Chat Demo")
st.markdown("- 🧠 BERT Sentiment Demo")
