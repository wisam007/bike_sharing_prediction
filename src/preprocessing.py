from typing import Any
import pandas as pd

LEAKAGE_COLUMNS = [
    "instant",
    "dteday",
    "casual",
    "registered",
    "atemp",
]

SEASON_MAP = {
    1: "spring",
    2: "summer",
    3: "fall",
    4: "winter",
}

WEATHER_MAP = {
    1: "clear",
    2: "mist_cloudy",
    3: "light_rain_snow",
    4: "heavy_rain_snow",
}

MONTH_MAP = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec",
}

WEEKDAY_MAP = {
    0: "sun",
    1: "mon",
    2: "tue",
    3: "wed",
    4: "thu",
    5: "fri",
    6: "sat",
}


def check_data_quality(df:pd.DataFrame)-> Any:
    """
    Compute basic data quality metrics.
    """

    return {
        "missing_values":int(df.isna().sum().sum()),
        "duplicated_rows":int(df.duplicated().sum())
    }

def fix_zero_humidity(df:pd.DataFrame)->pd.DataFrame:
    """
    Replace zero humidity values with the median
    humidity of the corresponding month.
    """

    df = df.copy()

    month_medians = (
        df.groupby("mnth")["hum"].transform(lambda x:x[x > 0].median())
    )
    mask = df["hum"] == 0

    df.loc[mask,"hum"] = month_medians[mask]

    return df
def check_target_leakage(df: pd.DataFrame) -> bool:
    """
    Verify that casual + registered equals cnt.
    """
    return bool(
        (df["casual"] + df["registered"] == df["cnt"]).all()
    )

def drop_unused_columns(df: pd.DataFrame,) -> pd.DataFrame:

    """
    Remove leakage and unnecessary columns.
    """
    return df.drop(columns=LEAKAGE_COLUMNS)

def map_categorical_values(df: pd.DataFrame,) -> pd.DataFrame:

    df = df.copy()

    df["season"] = df["season"].map(SEASON_MAP)
    df["weathersit"] = df["weathersit"].map(WEATHER_MAP)
    df["mnth"] = df["mnth"].map(MONTH_MAP)
    df["weekday"] = df["weekday"].map(WEEKDAY_MAP)

    return df

def preprocess_data(df: pd.DataFrame,) -> tuple[pd.DataFrame, dict]:

    quality = check_data_quality(df)

    df = fix_zero_humidity(df)

    leakage_ok = check_target_leakage(df)

    if not leakage_ok:
        raise ValueError(
            "Target leakage validation failed."
        )

    df = drop_unused_columns(df)

    df = map_categorical_values(df)

    return df, quality