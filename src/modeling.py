from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    ExtraTreesRegressor,
    AdaBoostRegressor,
)
from sklearn.svm import SVR

import time

from sklearn.pipeline import Pipeline


def get_models() -> dict:

    return {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(alpha=1.0),
        "Lasso Regression": Lasso(alpha=1.0, max_iter=5000),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(
            n_estimators=100,
            random_state=42,
        ),
        "Gradient Boosting": GradientBoostingRegressor(
            random_state=42,
        ),
        "Support Vector Regressor": SVR(
            C=1000,
            epsilon=10,
        ),
        "Extra Trees": ExtraTreesRegressor(
            random_state=42,
        ),
        "AdaBoost": AdaBoostRegressor(
            random_state=42,
        ),
    }



def train_model(
    model,
    preprocessor,
    X_train,
    y_train,
):

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", model),
    ])

    start = time.perf_counter()

    pipeline.fit(X_train, y_train)

    elapsed = time.perf_counter() - start

    return pipeline, elapsed
