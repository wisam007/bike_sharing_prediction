from pathlib import Path
import pandas as pd

def load_data(filepath: Path) -> pd.DataFrame:
        """
    Load the bike-sharing dataset.

    Parameters
    ----------
    filepath : Path
        Location of the CSV file.

    Returns
    -------
    pd.DataFrame
    """
        return pd.read_csv(filepath)