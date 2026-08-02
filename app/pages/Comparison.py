import streamlit as st

from src.utils import load_comparison_dataframe

st.set_page_config(page_title="Comparison", page_icon="📊")

st.title("Model Comparison")

comparison_df = load_comparison_dataframe()

st.dataframe(comparison_df, use_container_width=True)

st.subheader("Key metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("MAE", f"{comparison_df.iloc[0]['MAE']:.2f}")
col2.metric("MSE", f"{comparison_df.iloc[0]['MSE']:.2f}")
col3.metric("RMSE", f"{comparison_df.iloc[0]['RMSE']:.2f}")
col4.metric("R²", f"{comparison_df.iloc[0]['Test R²']:.4f}")
