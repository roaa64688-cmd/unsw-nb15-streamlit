# UNSW-NB15 Streamlit Deployment

## Files
- `app.py` — Streamlit interface.
- `final_model.pkl` — saved model bundle.
- `requirements.txt` — required Python packages.

## Important
The model file must be created from the training notebook/script. The original project contains a final line attempting to save `final_model`, but `final_model` is not defined in the provided file.

Before deployment, run the training code and save a bundle like this:

```python
import joblib

deployment_bundle = {
    "model": opt_search.best_estimator_,
    "encoder": ordinal_encoder,
    "feature_columns": X_train.columns.tolist(),
    "categorical_cols": ["proto", "service", "state"],
    "numeric_cols": numerical_cols,
}

joblib.dump(deployment_bundle, "final_model.pkl")
```

Also, in the training code, keep the original `OrdinalEncoder` under the name `ordinal_encoder` because the variable `encoder` is later reused for `OneHotEncoder`.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Cloud
Upload `app.py`, `final_model.pkl`, and `requirements.txt` to the GitHub repository, then create a Streamlit app using `app.py` as the main file.
