import streamlit as st

from src.train import train_and_evaluate

st.set_page_config(page_title="Model", page_icon="🧠")

st.title("Model Information")

with st.spinner("Training and evaluating the notebook models..."):
    result = train_and_evaluate()

results_df = result["results_df"]

st.subheader("Preprocessing steps")
st.write("The modular pipeline preserves the notebook's data preparation steps: zero-humidity repair, removal of leakage columns, categorical mapping, scaling, and one-hot encoding.")

st.subheader("Algorithms compared")
st.dataframe(results_df[["Model", "Train R²", "Test R²", "MAE", "RMSE"]], use_container_width=True)

st.subheader("Best model")
st.success(f"Selected model: {result['best_model_name']}")
st.write("The best model was chosen by the notebook's evaluation logic using the highest test R² score.")

st.caption(f"Saved artifact: {result['comparison_path']}")
