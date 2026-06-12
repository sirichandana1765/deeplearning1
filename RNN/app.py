import streamlit as st


st.set_page_config(page_title="RNN Demo", page_icon="🔁", layout="wide")

st.markdown(
    """
    <style>
        :root { color-scheme: dark; }
        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #09131f 0%, #132a40 45%, #1d3b5c 100%);
        }
        [data-testid="stAppViewContainer"] > .main { background: transparent; }
        .block-container { padding-top: 1.4rem; padding-bottom: 2rem; }
        .glass {
            background: rgba(6, 12, 24, 0.78);
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

st.title("🔁 Recurrent Neural Network (RNN) Demo")
st.caption("A simple interactive page showing how sequence information flows through an RNN.")

col1, col2 = st.columns([1.0, 1.0], gap="large")

with col1:
    st.markdown("""
    <div class="glass">
        <h3 style='margin-top:0;'>Why RNNs matter</h3>
        <p>RNNs process sequences step by step, keeping a hidden state that remembers what came before. That makes them useful for time series, language, and speech tasks.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    sequence_len = st.slider("Sequence length", 2, 10, 6)
    memory_strength = st.slider("Memory strength", 0, 10, 7)
    input_signal = st.slider("Input signal", 0, 10, 5)

    recurrent_score = (0.45 * sequence_len) + (0.35 * memory_strength) + (0.20 * input_signal)
    confidence = round(min(recurrent_score * 5, 100), 1)
    label = "Strong temporal pattern" if confidence >= 70 else "Moderate temporal pattern"

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.metric("RNN score", f"{confidence}%")
    st.metric("Interpretation", label)
    st.progress(min(confidence / 100, 1.0))
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.subheader("RNN intuition")
st.write("The hidden state at each step is updated using the current input and past context, which is the core idea behind recurrent models.")
st.code("hidden_state = f(previous_state, current_input)", language="python")
st.markdown("</div>", unsafe_allow_html=True)
