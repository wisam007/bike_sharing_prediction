import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Feature Importance", page_icon="🎯")

st.title("Feature Importance")

feature_importance_path = Path("artifacts/feature_importance.csv")
if feature_importance_path.exists():
    df = pd.read_csv(feature_importance_path)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Feature importance report is available after training. The current project stores an empty placeholder until the model is retrained.")
