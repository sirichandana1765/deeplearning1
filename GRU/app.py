import streamlit as st


st.set_page_config(page_title="GRU Demo", page_icon="⚙️", layout="wide")

st.markdown(
    """
    <style>
        :root { color-scheme: dark; }
        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #111827 0%, #172554 45%, #312e81 100%);
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

st.title("⚙️ Gated Recurrent Unit (GRU) Demo")
st.caption("A compact recurrent unit that balances efficiency and sequence learning.")

col1, col2 = st.columns([1.0, 1.0], gap="large")

with col1:
    st.markdown("""
    <div class="glass">
        <h3 style='margin-top:0;'>Why GRUs are popular</h3>
        <p>GRUs simplify the LSTM design by using reset and update gates. This makes them faster and often easier to train while still handling sequential context well.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    sequence_len = st.slider("Sequence length", 2, 10, 6)
    update_rate = st.slider("Update rate", 0, 10, 7)
    reset_rate = st.slider("Reset rate", 0, 10, 4)

    gru_score = (0.35 * sequence_len) + (0.35 * update_rate) + (0.30 * reset_rate)
    confidence = round(min(gru_score * 5.5, 100), 1)
    label = "Efficient sequence modeling" if confidence >= 70 else "Solid sequence modeling"

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.metric("GRU score", f"{confidence}%")
    st.metric("Interpretation", label)
    st.progress(min(confidence / 100, 1.0))
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.subheader("GRU intuition")
st.write("GRUs use update and reset gates to decide how much previous context should be carried forward.")
st.code("hidden_state = update_gate * candidate + (1 - update_gate) * previous_state", language="python")
st.markdown("</div>", unsafe_allow_html=True)
