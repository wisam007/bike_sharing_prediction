import pandas as pd


def predict(model, data: pd.DataFrame):
    """
    Predict bike rental counts using a trained pipeline.

    Parameters
    ----------
    model : sklearn Pipeline
        Trained pipeline containing preprocessing and model.

    data : pd.DataFrame
        New observations.

    Returns
    -------
    numpy.ndarray
        Predicted bike rental counts.
    """
    return model.predict(data)