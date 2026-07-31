from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error,
    r2_score,
)

import numpy as np

def adjusted_r2(
    r2,
    n,
    p,
):

    return 1 - (1 - r2) * (n - 1) / (n - p - 1)


def evaluate_model(
    pipeline,
    X_train,
    X_test,
    y_train,
    y_test,
    training_time,
    model_name,
):
    y_pred = pipeline.predict(X_test)

    results = {
        "Model": model_name,
        "Training Time (s)": round(training_time, 4),
        "MAE": mean_absolute_error(y_test, y_pred),
        "MSE": mean_squared_error(y_test, y_pred),
        "MAPE":mean_absolute_percentage_error(y_test,y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
        "R2": r2_score(y_test, y_pred),
    }

    return results