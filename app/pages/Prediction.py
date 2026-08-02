import streamlit as st

from src.predict import predict_from_inputs
from src.data_loader import load_dataset
from src.feature_engineering import clean_dataset

st.set_page_config(page_title="Prediction", page_icon="🔮")

st.title("Prediction")

st.write("Enter the feature values below to generate a bike rental estimate using the trained pipeline.")

raw_df = load_dataset()
clean_df = clean_dataset(raw_df)

season_options = sorted(clean_df["season"].unique().tolist())
month_options = sorted(clean_df["mnth"].unique().tolist())
weather_options = sorted(clean_df["weathersit"].unique().tolist())
weekday_options = sorted(clean_df["weekday"].unique().tolist())

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        season = st.selectbox("Season", season_options)
        month = st.selectbox("Month", month_options)
        weather = st.selectbox("Weather", weather_options)
        weekday = st.selectbox("Weekday", weekday_options)
        year = st.selectbox("Year", [0, 1], format_func=lambda value: "2011" if value == 0 else "2012")
    with col2:
        holiday = st.checkbox("Holiday")
        workingday = st.checkbox("Working Day")
        temp = st.slider("Temperature", min_value=float(clean_df["temp"].min()), max_value=float(clean_df["temp"].max()), value=float(clean_df["temp"].median()), step=0.01)
        humidity = st.slider("Humidity", min_value=float(clean_df["hum"].min()), max_value=float(clean_df["hum"].max()), value=float(clean_df["hum"].median()), step=0.01)
        windspeed = st.slider("Windspeed", min_value=float(clean_df["windspeed"].min()), max_value=float(clean_df["windspeed"].max()), value=float(clean_df["windspeed"].median()), step=0.01)

    submitted = st.form_submit_button("Predict Rental Count")

if submitted:
    payload = {
        "season": season,
        "mnth": month,
        "weathersit": weather,
        "weekday": weekday,
        "yr": year,
        "holiday": int(holiday),
        "workingday": int(workingday),
        "temp": temp,
        "hum": humidity,
        "windspeed": windspeed,
    }
    prediction = predict_from_inputs(payload)

    st.markdown(
        f"""
        <div style="background: linear-gradient(90deg, #0f766e, #14b8a6); padding: 1.5rem; border-radius: 1rem; text-align: center;">
            <h2 style="color: white; margin: 0;">Predicted Bike Rental Count</h2>
            <h1 style="color: white; margin: 0.2rem 0 0;">{prediction:,.1f}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
