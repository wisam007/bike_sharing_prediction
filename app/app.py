import streamlit as st

from src.data_loader import load_dataset

st.set_page_config(page_title="Bike Sharing Prediction", page_icon="🚲", layout="wide")

st.markdown(
    """
    <div style="background: linear-gradient(90deg, #0f172a, #2563eb); padding: 2rem; border-radius: 1rem;">
        <h1 style="color: white; margin: 0;">Bike Sharing Demand Prediction</h1>
        <p style="color: #dbeafe; margin-top: 0.5rem;">A production-style modular ML project for forecasting daily bike rentals.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

st.subheader("Project overview")
st.write(
    "This application packages the notebook workflow into a modular, production-ready project. "
    "It loads the bike sharing dataset, trains the same regression pipeline from the notebook, "
    "and exposes the model through an interactive prediction experience."
)

st.info("Use the sidebar navigation to explore the project, dataset, model details, and prediction workflow.")

with st.expander("Dataset snapshot", expanded=True):
    df = load_dataset()
    st.dataframe(df.head(), use_container_width=True)
    st.caption(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
