import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Network Intrusion Detection")

st.write(
    "Enter network traffic features to predict whether the connection is Normal or an Attack."
)


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


model = bundle["model"]
encoder = bundle["encoder"]
feature_columns = bundle["feature_columns"]
cat_cols = bundle["categorical_cols"]
numeric_cols = bundle["numeric_cols"]


st.subheader("🔹 Categorical Features")
