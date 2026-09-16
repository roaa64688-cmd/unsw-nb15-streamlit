# ==========================================
# FINAL MODEL + DEPLOYMENT FILE
# Run this AFTER opt_search has finished.
# ==========================================

import joblib

# IMPORTANT:
# In the preprocessing section, rename:
#     encoder = OrdinalEncoder(...)
# to:
#     ordinal_encoder = OrdinalEncoder(...)
#
# Then use:
#     X_train[cat_cols] = ordinal_encoder.fit_transform(X_train[cat_cols])
#     X_test[cat_cols] = ordinal_encoder.transform(X_test[cat_cols])
#
# The optimization in the provided project is performed on X_train/y_train,
# so the optimized estimator can be saved directly.

final_model = opt_search.best_estimator_

deployment_bundle = {
    "model": final_model,
    "encoder": ordinal_encoder,
    "feature_columns": X_train.columns.tolist(),
    "categorical_cols": cat_cols,
    "numeric_cols": numerical_cols,
}

joblib.dump(deployment_bundle, "final_model.pkl")

print("✅ final_model.pkl created successfully!")
