import streamlit as st

st.header("Project description")
st.write(
    "This project addresses a classic regression problem: predicting the daily bike rental count from weather, seasonal, and calendar features."
)

st.space("medium")

cols = st.columns(2)

with cols[0].container(border=True, height="stretch"):
    st.markdown("#### :material/business: Business context")
    st.write(
        "Bike sharing operators need reliable demand forecasts to manage fleet distribution, "
        "optimize staffing, and schedule maintenance. "
        "Accurate daily rental estimates help prevent stockouts (empty stations) and overages (full stations), "
        "improving user satisfaction and operational efficiency."
    )

with cols[1].container(border=True, height="stretch"):
    st.markdown("#### :material/track_changes: Project objectives")
    st.write(
        "The core objective is to build a machine learning pipeline that maps environmental conditions "
        "(temperature, humidity, windspeed) and date categories (season, weekday, holiday) to target demand. "
        "The model must provide accurate predictions and serve them through a clean user interface."
    )

st.space("medium")

with st.container(border=True):
    st.markdown("#### :material/sync: Machine learning workflow")
    st.markdown(
        "- **Data extraction & cleaning**: Preprocess raw dataset and fix issues like zero humidity values.\n"
        "- **Feature preparation**: Define numerical pipelines (scaling), categorical pipelines (encoding), and passthrough fields.\n"
        "- **Model training**: Train several candidate regression models (Linear Regression, SVR, Random Forest, etc.).\n"
        "- **Evaluation**: Compare models based on $R^2$, RMSE, and MAE.\n"
        "- **Inference**: Persist and deploy the best performing pipeline for real-time predictions."
    )
