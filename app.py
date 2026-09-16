import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Network Intrusion Detection")
st.write("Enter network traffic features to predict whether the connection is Normal or an Attack.")
import os
import joblib

@st.cache_resource
def load_bundle():
    model_path = os.path.join(os.path.dirname(__file__), "final_model.pkl")
    return joblib.load(model_path)
try:
    bundle = load_bundle()
except Exception as e:
    st.error(f"Model loading error: {type(e).__name__}: {e}")
    st.stop()

model = bundle["model"]
encoder = bundle["encoder"]
feature_columns = bundle["feature_columns"]
cat_cols = bundle["categorical_cols"]
numeric_cols = bundle["numeric_cols"]

st.subheader("🔹 Categorical Features")
c1, c2, c3 = st.columns(3)

def get_options(col):
    try:
        return list(encoder.categories_[cat_cols.index(col)])
    except Exception:
        return []

with c1:
    proto = st.selectbox("Protocol (proto)", get_options("proto"))
with c2:
    service = st.selectbox("Service", get_options("service"))
with c3:
    state = st.selectbox("State", get_options("state"))

st.subheader("🔹 Numerical Features")

# Default value 0 keeps the form easy to use.
values = {}
cols = st.columns(3)

for i, col in enumerate(numeric_cols):
    with cols[i % 3]:
        values[col] = st.number_input(
            col,
            value=0.0,
            format="%.6f"
        )

if st.button("🔍 Detect Intrusion", use_container_width=True):
    input_df = pd.DataFrame([values])
    input_df.insert(0, "proto", proto)
    input_df.insert(1, "service", service)
    input_df.insert(2, "state", state)

    input_df = input_df[feature_columns]

    # The saved model was trained after ordinal encoding.
    input_df[cat_cols] = encoder.transform(input_df[cat_cols])

    prediction = model.predict(input_df)[0]

    if hasattr(model, "predict_proba"):
        probability = float(model.predict_proba(input_df)[0][1])
    else:
        probability = None

    st.divider()

    if int(prediction) == 1:
        st.error("🔴 ATTACK DETECTED")
        if probability is not None:
            st.write(f"Attack probability: **{probability:.2%}**")
    else:
        st.success("🟢 NORMAL TRAFFIC")
        if probability is not None:
            st.write(f"Attack probability: **{probability:.2%}**")

st.caption("UNSW-NB15 Machine Learning Project")
