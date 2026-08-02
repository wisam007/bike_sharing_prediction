import streamlit as st
import json
import pandas as pd
from config import TABLE_DIR, JSON_DIR

st.header("Project reports")
st.write(
    "This page aggregates the data quality and model evaluation reports generated during the training pipeline run."
)

st.space("medium")

quality_path = JSON_DIR / "data_quality.json"
summary_path = JSON_DIR / "dataset_summary.json"

st.subheader("Data quality & summary report")
cols = st.columns(2)

with cols[0].container(border=True, height="stretch"):
    st.markdown("#### :material/fact_check: Quality checks")
    if quality_path.exists():
        with open(quality_path, "r") as f:
            quality = json.load(f)
        st.metric("Missing values found", quality.get("missing_values", 0), delta="0 expected", delta_color="normal")
        st.metric("Duplicate rows found", quality.get("duplicated_rows", 0), delta="0 expected", delta_color="normal")
    else:
        st.caption("Quality check file data_quality.json not found.")

with cols[1].container(border=True, height="stretch"):
    st.markdown("#### :material/info: Dataset shape details")
    if summary_path.exists():
        with open(summary_path, "r") as f:
            summary = json.load(f)
        st.metric("Total rows loaded", f"{summary.get('rows', 0):,}")
        st.metric("Total raw columns", summary.get("columns", 0))
    else:
        st.caption("Summary check file dataset_summary.json not found.")

st.space("medium")

stats_path = TABLE_DIR / "descriptive_statistics.csv"
if stats_path.exists():
    with st.expander("Descriptive statistics table (day.csv)", icon=":material/table_rows:"):
        stats_df = pd.read_csv(stats_path, index_col=0)
        st.dataframe(stats_df)
else:
    st.info("Descriptive statistics table not found.", icon=":material/info:")
