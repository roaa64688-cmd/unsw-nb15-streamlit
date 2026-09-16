import os
import joblib
import pandas as pd
import streamlit as st


# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)


# =========================
# Title
# =========================
st.title("🛡️ Network Intrusion Detection")

st.write(
    "Enter network traffic features to predict whether "
    "the connection is Normal or an Attack."
)


# =========================
# Load Model
# =========================
@st.cache_resource
def load_bundle():

    model_path = os.path.join(
        os.path.dirname(__file__),
        "final_model.pkl"
    )

    return joblib.load(model_path)


try:

    bundle = load_bundle()

except Exception as e:

    st.error(
        f"Model loading error: {type(e).__name__}: {e}"
    )

    st.stop()


# =========================
# Get Model Components
# =========================
model = bundle["model"]

encoder = bundle["encoder"]

feature_columns = bundle["feature_columns"]

cat_cols = bundle["categorical_cols"]


# =========================
# Categorical Features
# =========================
st.subheader("🔹 Categorical Features")

col1, col2, col3 = st.columns(3)

with col1:
    proto = st.text_input(
        "Protocol (proto)",
        value="tcp"
    )

with col2:
    service = st.text_input(
        "Service",
        value="http"
    )

with col3:
    state = st.text_input(
        "State",
        value="FIN"
    )


# =========================
# Numeric Features
# =========================
st.subheader("🔹 Numeric Features")

numeric_cols = [
    col for col in feature_columns
    if col not in cat_cols
]

input_data = {}

columns = st.columns(3)

for i, col in enumerate(numeric_cols):

    with columns[i % 3]:

        input_data[col] = st.number_input(
            col,
            value=0.0
        )


# =========================
# Prediction
# =========================
if st.button("🔍 Predict", use_container_width=True):

    # Create DataFrame
    data = pd.DataFrame([input_data])

    # Add categorical values
    data["proto"] = proto
    data["service"] = service
    data["state"] = state

    # Encode categorical columns
    data[cat_cols] = encoder.transform(
        data[cat_cols]
    )

    # Make sure columns have the same order
    data = data[feature_columns]

    # Prediction
    prediction = model.predict(data)[0]

    # Display result
    if prediction == 1:

        st.error(
            "⚠️ Attack Detected"
        )

    else:

        st.success(
            "✅ Normal Traffic"
        )
