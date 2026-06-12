import streamlit as st


st.set_page_config(page_title="LSTM Demo", page_icon="🧠", layout="wide")

st.markdown(
    """
    <style>
        :root { color-scheme: dark; }
        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0f172a 0%, #111827 45%, #1f2937 100%);
        }
        [data-testid="stAppViewContainer"] > .main { background: transparent; }
        .block-container { padding-top: 1.4rem; padding-bottom: 2rem; }
        .glass {
            background: rgba(8, 15, 30, 0.78);
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

st.title("🧠 Long Short-Term Memory (LSTM) Demo")
st.caption("Explore how LSTM cells use gates to manage short- and long-term information flow.")

col1, col2 = st.columns([1.0, 1.0], gap="large")

with col1:
    st.markdown("""
    <div class="glass">
        <h3 style='margin-top:0;'>Why LSTM stands out</h3>
        <p>LSTM networks use input, forget, and output gates to decide what to keep, update, or pass forward. This helps them handle long sequences better than basic RNNs.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    memory_depth = st.slider("Sequence depth", 1, 10, 5)
    forget_bias = st.slider("Forget bias", 0, 10, 6)
    update_strength = st.slider("Update strength", 0, 10, 7)

    lstm_score = (0.40 * memory_depth) + (0.30 * forget_bias) + (0.30 * update_strength)
    confidence = round(min(lstm_score * 6, 100), 1)
    label = "Stable long-range memory" if confidence >= 70 else "Moderate long-range memory"

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.metric("LSTM score", f"{confidence}%")
    st.metric("Interpretation", label)
    st.progress(min(confidence / 100, 1.0))
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.subheader("LSTM intuition")
st.write("The gates in an LSTM cell decide what information should be remembered or forgotten through time.")
st.code("forget_gate, input_gate, output_gate = ...", language="python")
st.markdown("</div>", unsafe_allow_html=True)
