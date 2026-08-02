import pandas as pd
import streamlit as st
# from config import RAW_DATA
# from src.loader import load_data

import json
from pathlib import Path

import pandas as pd
import streamlit as st

from config import JSON_DIR, TABLE_DIR, PROCESSED_DATA



@st.cache_data(ttl="1h", max_entries=5)
@st.cache_data
def load_json_file(path):

    with open(path, "r") as file:
        return json.load(file)


@st.cache_data
def load_statistics():

    return pd.read_csv(
        TABLE_DIR / "descriptive_statistics.csv"
    )


@st.cache_data
def load_processed_dataset():

    return pd.read_csv(
        PROCESSED_DATA
    )


st.header("Dataset Information")


try:

    summary = load_json_file(
        JSON_DIR / "dataset_summary.json"
    )

    quality = load_json_file(
        JSON_DIR / "data_quality.json"
    )


    # ------------------------
    # Dataset Overview
    # ------------------------

    st.subheader("Dataset Overview")


    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            "Rows",
            f"{summary['rows']:,}"
        )


    with col2:
        st.metric(
            "Columns",
            summary["columns"]
        )


    with col3:
        st.metric(
            "Target",
            summary["target"]
            if "target" in summary
            else "cnt"
        )


    st.write(
        "Problem Type: **Regression**"
    )

    st.write(
        "Dataset: **Bike Sharing Demand**"
    )


    st.divider()


    # ------------------------
    # Data Quality
    # ------------------------

    st.subheader("Data Quality")


    q1, q2 = st.columns(2)


    with q1:

        st.metric(
            "Missing Values",
            quality["missing_values"]
        )


    with q2:

        st.metric(
            "Duplicate Rows",
            quality["duplicated_rows"]
        )


    st.divider()


    # ------------------------
    # Data Types
    # ------------------------

    st.subheader("Feature Data Types")


    dtype_df = pd.DataFrame(
        summary["data_types"].items(),
        columns=[
            "Feature",
            "Data Type"
        ]
    )


    st.dataframe(
        dtype_df,
        use_container_width=True
    )


    st.divider()


    # ------------------------
    # Statistics
    # ------------------------

    st.subheader(
        "Descriptive Statistics"
    )


    stats = load_statistics()


    st.dataframe(
        stats,
        use_container_width=True
    )


    st.divider()


    # ------------------------
    # Processed Dataset Preview
    # ------------------------

    st.subheader(
        "Processed Dataset Preview"
    )


    processed = load_processed_dataset()


    st.dataframe(
        processed.head(10),
        use_container_width=True
    )


except Exception as e:

    st.error(
        f"Failed to load dataset information: {e}"
    )
except Exception as e:
    st.error(f"Failed to load dataset: {e}", icon=":material/error:")
