import streamlit as st

st.set_page_config(page_title="Project", page_icon="📘")

st.title("Project Description")
st.write(
    "This project addresses a classic regression problem: predicting the daily bike rental count from weather, seasonal, and calendar features."
)

st.subheader("Business problem")
st.write(
    "Bike sharing operators need reliable forecasts to manage fleet distribution, staffing, and maintenance planning. "
    "Accurate rental demand estimates help reduce shortages and improve operational efficiency."
)

st.subheader("Objective")
st.write("Build a regression model that predicts the total number of daily rentals using historical patterns and environmental conditions.")

st.subheader("Workflow")
st.markdown(
    "- Load and clean the dataset\n"
    "- Engineer the feature set from the notebook\n"
    "- Train and compare multiple regression models\n"
    "- Persist the best pipeline for inference\n"
    "- Serve predictions through a Streamlit interface"
)
