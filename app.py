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
st.subheader("🔹 Categorical Features")  عدلي الكود دا

أيوه، عندك مشكلة indentation واضحة في الكود، وكمان فيه import os وimport joblib مكررين.

خلي app.py بالشكل ده بالضبط:

import streamlit as st
import pandas as pd
import joblib
import os

# Page settings
st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)

# Title
st.title("🛡️ Network Intrusion Detection")
st.write(
    "Enter network traffic features to predict whether the connection is Normal or an Attack."
)


# Load model
@st.cache_resource
def load_bundle():
    model_path = os.path.join(
        os.path.dirname(__file__),
        "final_model.pkl"
    )
    return joblib.load(model_path)


# Try to load model
try:
    bundle = load_bundle()

except Exception as e:
    st.error(
        f"Model loading error: {type(e).__name__}: {e}"
    )
    st.stop()


# Get model components
model = bundle["model"]
encoder = bundle["encoder"]
feature_columns = bundle["feature_columns"]
cat_cols = bundle["categorical_cols"]
numeric_cols = bundle["numeric_cols"]


# Categorical features
st.subheader("🔹 Categorical Features")

@st.cache_resource
def load_bundle():
 model_path = ...
return joblib.load(model_path)
لازم return تكون جوه الـ function:

@st.cache_resource
def load_bundle():
    model_path = os.path.join(
        os.path.dirname(__file__),
        "final_model.pkl"
    )
    return joblib.load(model_path)
لاحظي المسافات قبل return.

دلوقتي اعملي الآتي
انسخي الكود اللي فوق كامل.

امسحي الكود القديم من app.py.

الصقي الكود الجديد.

اعملي Commit changes في GitHub.

افتحي Streamlit واضغطي Reboot app.

لو ظهر Error جديد، ابعتيهولي زي ما هو ومش تغيري أي حاجة تانية.


