import streamlit as st


st.set_page_config(
    page_title="ANN Demo",
    page_icon="🧠",
    layout="wide",
)

st.markdown(
    """
    <style>
        :root {
            color-scheme: dark;
        }
        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #07111f 0%, #10253a 45%, #1a3b63 100%);
        }
        [data-testid="stAppViewContainer"] > .main {
            background: transparent;
        }
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }
        .glass {
            background: rgba(8, 15, 30, 0.72);
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


st.title("🧠 Artificial Neural Network Demo")
st.caption("Explore a simple ANN-style prediction flow with an elegant Streamlit interface.")

col_left, col_right = st.columns([1.1, 0.9], gap="large")

with col_left:
    st.markdown(
        """
        <div class="glass">
            <h3 style='margin-top:0;'>Why this demo matters</h3>
            <p>Artificial neural networks learn patterns from input features and produce a prediction.
            This page uses a lightweight ANN-inspired scoring model to demonstrate how input values shape the output.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("How the ANN score is calculated", expanded=True):
        st.markdown(
            """
            - Each feature is weighted to represent a neuron input.
            - The model combines the values and applies a sigmoid-style activation.
            - The final score is converted into a simple performance label.
            """
        )

with col_right:
    st.markdown(
        """
        <div class="glass">
            <h3 style='margin-top:0;'>Live input panel</h3>
            <p>Adjust the sliders to see how the ANN-inspired score changes in real time.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    hours = st.slider("Study hours", 0, 10, 6)
    attendance = st.slider("Attendance (%)", 0, 100, 75)
    practice = st.slider("Practice score", 0, 10, 7)

    # Small ANN-inspired calculation for a friendly demo.
    weighted_sum = (
        0.35 * hours
        + 0.25 * (attendance / 10)
        + 0.40 * practice
    )
    activation = 1 / (1 + 2.718281828459045 ** (-weighted_sum))
    confidence = round(activation * 100, 1)

    if confidence >= 75:
        result = "Excellent performance"
    elif confidence >= 50:
        result = "Good performance"
    else:
        result = "Needs more practice"

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.metric("ANN score", f"{confidence}%")
    st.metric("Prediction", result)
    st.progress(min(confidence / 100, 1.0))
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.subheader("Model insight")
st.write(
    "This simplified ANN-style example shows how weighted inputs and activation produce a prediction. "
    "In a real neural network, hidden layers and training data make the model much more powerful."
)
st.code(
    """
weighted_sum = 0.35*hours + 0.25*(attendance/10) + 0.40*practice
activation = 1 / (1 + exp(-weighted_sum))
    """,
    language="python",
)
st.markdown("</div>", unsafe_allow_html=True)
