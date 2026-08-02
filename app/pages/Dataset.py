import pandas as pd
import streamlit as st

from src.data_loader import load_dataset

st.set_page_config(page_title="Dataset", page_icon="🧾")

st.title("Dataset Information")

raw_df = load_dataset()

col1, col2 = st.columns(2)
col1.metric("Rows", raw_df.shape[0])
col2.metric("Columns", raw_df.shape[1])

st.subheader("Feature descriptions")
feature_descriptions = {
    "season": "Seasonal category of the observation.",
    "yr": "Year indicator (0 = 2011, 1 = 2012).",
    "mnth": "Calendar month.",
    "holiday": "Whether the day is a holiday.",
    "weekday": "Day of the week.",
    "workingday": "Whether the day is a working day.",
    "weathersit": "Weather condition category.",
    "temp": "Normalized temperature reading.",
    "hum": "Normalized humidity reading.",
    "windspeed": "Normalized wind speed.",
    "cnt": "Target variable: total daily bike rentals.",
}

st.dataframe(pd.DataFrame(feature_descriptions.items(), columns=["Feature", "Description"]), use_container_width=True)

st.subheader("Sample dataframe")
st.dataframe(raw_df.head(), use_container_width=True)
