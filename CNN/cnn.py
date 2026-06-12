import streamlit as st


st.set_page_config(
    page_title="CNN Demo",
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
            background: linear-gradient(135deg, #08111d 0%, #10293d 45%, #183d5e 100%);
        }
        [data-testid="stAppViewContainer"] > .main {
            background: transparent;
        }
        .block-container {
            padding-top: 1.4rem;
            padding-bottom: 2rem;
        }
        .glass {
            background: rgba(7, 12, 24, 0.78);
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


st.title("🧠 Convolutional Neural Network Demo")
st.caption("A polished CNN-style interface to explore feature extraction and pattern recognition.")

col_left, col_right = st.columns([1.05, 0.95], gap="large")

with col_left:
    st.markdown(
        """
        <div class="glass">
            <h3 style='margin-top:0;'>What CNNs do well</h3>
            <p>Convolutional Neural Networks detect local patterns in images using filters, pooling, and deeper layers.
            This demo uses a simplified CNN-style score to show how texture, edges, and feature strength combine.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("CNN intuition", expanded=True):
        st.markdown(
            """
            - Filters scan small image regions for shapes and edges.
            - Pooling reduces the size while keeping important information.
            - The final features are used for classification or prediction.
            """
        )

with col_right:
    st.markdown(
        """
        <div class="glass">
            <h3 style='margin-top:0;'>Interactive CNN-style inputs</h3>
            <p>Move the sliders to see how a simplified convolutional score changes as image features become stronger.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    edge_strength = st.slider("Edge strength", 0, 10, 6)
    texture_density = st.slider("Texture density", 0, 10, 5)
    pattern_depth = st.slider("Pattern depth", 1, 5, 3)

    # Simplified CNN-style activation score.
    feature_map = (0.45 * edge_strength) + (0.30 * texture_density) + (0.25 * pattern_depth)
    activation = 1 / (1 + 2.718281828459045 ** (-feature_map))
    confidence = round(activation * 100, 1)

    if confidence >= 75:
        label = "Strong pattern match"
    elif confidence >= 50:
        label = "Moderate pattern match"
    else:
        label = "Low feature confidence"

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.metric("CNN score", f"{confidence}%")
    st.metric("Prediction", label)
    st.progress(min(confidence / 100, 1.0))
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.subheader("Model insight")
st.write(
    "This simplified CNN-style example mirrors how convolutional filters summarize local image features. "
    "In a real CNN, these features pass through multiple layers to detect complex visual patterns."
)
st.code(
    """
feature_map = 0.45*edge_strength + 0.30*texture_density + 0.25*pattern_depth
activation = 1 / (1 + exp(-feature_map))
    """,
    language="python",
)
st.markdown("</div>", unsafe_allow_html=True)
