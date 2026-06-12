import streamlit as st


st.set_page_config(page_title="BiLSTM Demo", page_icon="🔄", layout="wide")

st.markdown(
    """
    <style>
        :root { color-scheme: dark; }
        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0b1120 0%, #172554 45%, #312e81 100%);
        }
        [data-testid="stAppViewContainer"] > .main { background: transparent; }
        .block-container { padding-top: 1.4rem; padding-bottom: 2rem; }
        .glass {
            background: rgba(6, 10, 22, 0.78);
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

st.title("🔄 Bidirectional LSTM Demo")
st.caption("See how reading a sequence in both directions improves context understanding.")

col1, col2 = st.columns([1.0, 1.0], gap="large")

with col1:
    st.markdown("""
    <div class="glass">
        <h3 style='margin-top:0;'>Why bidirectional matters</h3>
        <p>A Bidirectional LSTM processes the sequence from left to right and right to left. This gives the model access to both past and future context.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    seq_len = st.slider("Sequence length", 2, 10, 6)
    context_strength = st.slider("Context strength", 0, 10, 8)
    direction_score = st.slider("Bidirectional coverage", 0, 10, 7)

    bilstm_score = (0.40 * seq_len) + (0.35 * context_strength) + (0.25 * direction_score)
    confidence = round(min(bilstm_score * 5.5, 100), 1)
    label = "Excellent context awareness" if confidence >= 75 else "Good context awareness"

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.metric("BiLSTM score", f"{confidence}%")
    st.metric("Interpretation", label)
    st.progress(min(confidence / 100, 1.0))
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.subheader("BiLSTM intuition")
st.write("The forward and backward LSTM layers combine their hidden states to create richer sequence representations.")
st.code("output = concat(forward_hidden, backward_hidden)", language="python")
st.markdown("</div>", unsafe_allow_html=True)
