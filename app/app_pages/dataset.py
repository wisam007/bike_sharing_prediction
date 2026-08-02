import pandas as pd
import streamlit as st
from config import RAW_DATA
from src.loader import load_data

@st.cache_data(ttl="1h", max_entries=5)
def get_raw_dataset() -> pd.DataFrame:
    """
    Load the raw bike sharing dataset and cache it.
    """
    return load_data(RAW_DATA)

st.header("Dataset information")

try:
    df = get_raw_dataset()
    
    cols = st.columns(2)
    with cols[0].container(border=True):
        st.metric("Total observations", f"{df.shape[0]:,}", icon=":material/format_list_bulleted:")
    with cols[1].container(border=True):
        st.metric("Total features", df.shape[1], icon=":material/view_column:")

    st.space("medium")
    
    st.subheader("Feature descriptions")
    feature_descriptions = {
        "season": "Seasonal category of the observation (spring, summer, fall, winter).",
        "yr": "Year indicator (0 = 2011, 1 = 2012).",
        "mnth": "Calendar month (jan, feb, mar, etc.).",
        "holiday": "Whether the day is a holiday (0 = No, 1 = Yes).",
        "weekday": "Day of the week (sun, mon, tue, etc.).",
        "workingday": "Whether the day is a working day (0 = No, 1 = Yes).",
        "weathersit": "Weather condition category (clear, mist_cloudy, light_rain_snow, heavy_rain_snow).",
        "temp": "Temperature in Celsius.",
        "hum": "Humidity percentage.",
        "windspeed": "Wind speed (km/h).",
        "cnt": "Target variable: total daily bike rentals (sum of casual and registered).",
    }
    
    desc_df = pd.DataFrame(feature_descriptions.items(), columns=["Feature name", "Description"])
    st.dataframe(desc_df)

    st.space("medium")
    
    st.subheader("Sample dataset preview")
    st.dataframe(df.head(10))

except Exception as e:
    st.error(f"Failed to load dataset: {e}", icon=":material/error:")
