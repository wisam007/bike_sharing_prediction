NUMERICAL_FEATURES = [
    "temp",
    "hum",
    "windspeed",
]

CATEGORICAL_FEATURES = [
    "season",
    "mnth",
    "weathersit",
    "weekday",
]

PASSTHROUGH_FEATURES = [
    "yr",
    "holiday",
    "workingday",
]

TARGET = "cnt"

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from sklearn.model_selection import train_test_split


def split_features_target(df:pd.DataFrame,):
    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    return X,y
def build_preprocessor() -> ColumnTransformer:
    numerical_pipeline = Pipeline([
        ("scalar",StandardScaler())
    ])
    categorical_pipeline  = Pipeline([("encoder",OneHotEncoder(drop="first",sparse_output=False,handle_unknown="ignore"))])


    preprocessor = ColumnTransformer(transformers=[
        ("num",numerical_pipeline,NUMERICAL_FEATURES),
        ("cat",categorical_pipeline,CATEGORICAL_FEATURES),
        ("pass","passthrough",PASSTHROUGH_FEATURES)
    ],verbose_feature_names_out=False)

    return preprocessor

def split_data(
        X,
        y,
        test_size=0.2,
        random_state=42,
        ):
    return train_test_split(X,y,test_size=test_size,random_state=random_state)
def get_feature_count(preprocessor, X_train) -> int:
    X_transformed = preprocessor.fit_transform(X_train)
    return X_transformed.shape[1]