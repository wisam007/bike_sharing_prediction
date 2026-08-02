import streamlit as st
import pandas as pd
import json
from config import JSON_DIR

st.header("Model comparison")
st.write(
    "A side-by-side comparison of candidate regression models based on standard evaluation metrics. "
    "Metrics are evaluated on the out-of-sample test set (20% of dataset)."
)

scores_path = JSON_DIR / "evalutaion_score.json"

if not scores_path.exists():
    st.warning("Model comparison data not found. Please train models first using: `python main.py`", icon=":material/warning:")
else:
    with open(scores_path, "r") as f:
        scores = json.load(f)
    
    comparison_df = pd.DataFrame(scores)
    
    st.subheader("Comparison matrix")
    st.dataframe(comparison_df[["Model", "R2", "MAE", "RMSE", "MSE", "MAPE", "Training Time (s)"]])

    st.space("medium")
    
    st.subheader("Leading model performance")
    best_model = comparison_df.iloc[0]
    
    with st.container(border=True):
        st.markdown(f"#### :material/leaderboard: Leader: **{best_model['Model']}**")
        st.write("Out-of-sample metrics for the champion model:")
        
        cols = st.columns(4)
        cols[0].metric("MAE", f"{best_model['MAE']:.2f}")
        cols[1].metric("RMSE", f"{best_model['RMSE']:.2f}")
        cols[2].metric("R² Score", f"{best_model['R2']:.4f}")
        cols[3].metric("MAPE", f"{best_model['MAPE'] * 100:.2f}%")
