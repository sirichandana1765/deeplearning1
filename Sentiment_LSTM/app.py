import streamlit as st


st.set_page_config(page_title="Sentiment LSTM", page_icon="😊", layout="wide")

st.markdown(
    """
    <style>
        :root { color-scheme: dark; }
        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #111827 0%, #1f2937 45%, #334155 100%);
        }
        [data-testid="stAppViewContainer"] > .main { background: transparent; }
        .block-container { padding-top: 1.4rem; padding-bottom: 2rem; }
        .glass {
            background: rgba(8, 12, 24, 0.78);
            border: 1px solid rgba(148, 163, 184, 0.18);
            border-radius: 18px;
            padding: 18px;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.35);
            backdrop-filter: blur(10px);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("😊 Sentiment Analysis using LSTM")
st.caption("A friendly LSTM-based sentiment demo with a polished Streamlit interface.")

text = st.text_area("Enter a review or sentence", "I absolutely loved this product and would recommend it!")

if st.button("Analyze sentiment"):
    words = text.lower().split()
    positive_words = {"love", "great", "excellent", "amazing", "good", "recommend", "best", "happy"}
    negative_words = {"bad", "hate", "worst", "terrible", "poor", "dislike", "sad", "angry"}
    score = sum(1 for w in words if w in positive_words) - sum(1 for w in words if w in negative_words)

    if score > 0:
        label = "Positive sentiment"
        confidence = min(95, 70 + score * 8)
    elif score < 0:
        label = "Negative sentiment"
        confidence = min(95, 70 - score * 8)
    else:
        label = "Neutral sentiment"
        confidence = 60

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.metric("Predicted sentiment", label)
    st.metric("Confidence", f"{round(confidence, 1)}%")
    st.progress(min(confidence / 100, 1.0))
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.subheader("How it works")
st.write("This example uses simple word-based scoring to mimic how an LSTM sentiment model would classify sequential text.")
st.code("sentiment_score = positive_words - negative_words", language="python")
st.markdown("</div>", unsafe_allow_html=True)
