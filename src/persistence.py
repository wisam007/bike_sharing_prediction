import joblib
from pathlib import Path


def save_model(model, filepath: Path):
    """
    Save a trained sklearn pipeline.
    """
    filepath.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, filepath)


def load_model(filepath: Path):
    """
    Load a trained sklearn pipeline.
    """
    return joblib.load(filepath)