from typing import Any
import pandas as pd

def dataset_summary(df:pd.DataFrame) -> dict[str,Any]:
    """Return a high-level summary of the dataset."""

    summary = {
        "rows": len(df),
        "columns":len(df.columns),
        "column_names":list(df.columns),
        "missing_values": df.isna().sum().to_dict(),
        "data_types":df.dtypes.astype(str).to_dict(),
    }
    return summary

def descriptive_statistics(df:pd.DataFrame)->pd.DataFrame:

    """Return descriptive statistics."""
    return df.describe(include="all")
def missing_value_report(df: pd.DataFrame) -> pd.Series:
    """Count missing values for each column."""
    return df.isna().sum()