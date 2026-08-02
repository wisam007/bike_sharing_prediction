import streamlit as st
import json
import pandas as pd
from config import JSON_DIR

st.header("Model training information")

best_model_path = JSON_DIR / "best_model.json"
scores_path = JSON_DIR / "evalutaion_score.json"

if not best_model_path.exists() or not scores_path.exists():
    st.warning("Training outputs not found. Please run the model training pipeline first using: `python main.py`", icon=":material/warning:")
else:
    with open(best_model_path, "r") as f:
        best_model = json.load(f)
        
    with open(scores_path, "r") as f:
        scores = json.load(f)
        
    scores_df = pd.DataFrame(scores)

    st.subheader("Preprocessing steps")
    st.write(
        "The model uses a clean, integrated scikit-learn preprocessing pipeline:\n"
        "- **Numerical variables** (`temp`, `hum`, `windspeed`) are scaled using `StandardScaler`.\n"
        "- **Categorical variables** (`season`, `mnth`, `weathersit`, `weekday`) are encoded using `OneHotEncoder(drop='first', sparse_output=False)`.\n"
        "- **Passthrough variables** (`yr`, `holiday`, `workingday`) are kept as-is."
    )

    st.space("medium")
    
    st.subheader("Candidate models compared")
    st.write(
        "The modeling step evaluated several regression algorithms. Below is the performance of each model, sorted by highest R² score:"
    )
    
    display_df = scores_df[["Model", "R2", "RMSE", "MAE", "Training Time (s)"]].rename(
        columns={
            "R2": "R² Score",
            "RMSE": "RMSE",
            "MAE": "MAE",
            "Training Time (s)": "Training Time (sec)"
        }
    )
    st.dataframe(display_df)

    st.space("medium")
    
    st.subheader("Best model selection")
    with st.container(border=True):
        st.markdown(f"#### :material/stars: Selected best model: **{best_model['Model']}**")
        st.write(
            "This model achieved the highest test R² score and was persisted to the model directory."
        )
        
        cols = st.columns(4)
        cols[0].metric("R² Score", f"{best_model['R2']:.4f}")
        cols[1].metric("RMSE", f"{best_model['RMSE']:.2f}")
        cols[2].metric("MAE", f"{best_model['MAE']:.2f}")
        cols[3].metric("Train Time", f"{best_model['Training Time']:.4f}s")
