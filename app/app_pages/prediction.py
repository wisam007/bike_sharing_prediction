import streamlit as st
import pandas as pd
from config import MODEL_PATH
from src.persistence import load_model
from src.inference import predict

@st.cache_resource
def get_model_pipeline():
    """
    Load the persisted pipeline model and cache it.
    """
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Trained model pipeline not found at {MODEL_PATH}")
    return load_model(MODEL_PATH)

st.header("Prediction portal")
st.write("Enter the weather and calendar settings below to estimate the total count of bike rentals.")

st.space("medium")

try:
    model = get_model_pipeline()
    model_loaded = True
except Exception as e:
    st.error(f"Model loading failed: {e}. Please ensure that the training pipeline has run and `model/bike_pipeline.pkl` is generated.", icon=":material/error:")
    model_loaded = False

if model_loaded:
    with st.form("prediction_form", border=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### :material/calendar_today: Temporal & calendar features")
            
            year_label = st.segmented_control("Year", ["2018", "2019"], default="2018")
            yr = 0 if year_label == "2018" else 1
            
            season_label = st.selectbox(
                "Season",
                ["Spring", "Summer", "Fall", "Winter"],
                index=0
            )
            season = season_label.lower()
            
            month_label = st.selectbox(
                "Month",
                ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                index=2
            )
            month_map = {
                "January": "jan", "February": "feb", "March": "mar", "April": "apr",
                "May": "may", "June": "jun", "July": "jul", "August": "aug",
                "September": "sep", "October": "oct", "November": "nov", "December": "dec"
            }
            mnth = month_map[month_label]
            
            weekday_label = st.selectbox(
                "Day of week",
                ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                index=5
            )
            weekday = weekday_label[:3].lower()
            
            with st.container(gap="small"):
                holiday_bool = st.toggle("Is holiday?", value=False)
                holiday = 1 if holiday_bool else 0
                
                workingday_bool = st.toggle("Is working day?", value=True)
                workingday = 1 if workingday_bool else 0
                
        with col2:
            st.markdown("#### :material/thermostat: Weather & atmospheric features")
            
            weather_label = st.selectbox(
                "Weather condition",
                [
                    "Clear / Partly Cloudy",
                    "Mist / Cloudy",
                    "Light Rain / Snow / Thunderstorm",
                    "Heavy Rain / Ice / Snow / Fog"
                ],
                index=0
            )
            weather_map = {
                "Clear / Partly Cloudy": "clear",
                "Mist / Cloudy": "mist_cloudy",
                "Light Rain / Snow / Thunderstorm": "light_rain_snow",
                "Heavy Rain / Ice / Snow / Fog": "heavy_rain_snow"
            }
            weathersit = weather_map[weather_label]
            
            temp = st.slider(
                "Temperature (°C)",
                min_value=2.5,
                max_value=35.0,
                value=20.0,
                step=0.1
            )
            
            hum = st.slider(
                "Humidity (%)",
                min_value=0.0,
                max_value=100.0,
                value=60.0,
                step=0.5
            )
            
            windspeed = st.slider(
                "Wind speed (km/h)",
                min_value=0.0,
                max_value=50.0,
                value=12.0,
                step=0.5
            )

        st.space("medium")
        
        submitted = st.form_submit_button("Predict bike rentals", icon=":material/online_prediction:", type="primary")

    if submitted:
        input_data = pd.DataFrame([
            {
                "season": season,
                "yr": yr,
                "mnth": mnth,
                "holiday": holiday,
                "weekday": weekday,
                "workingday": workingday,
                "weathersit": weathersit,
                "temp": temp,
                "hum": hum,
                "windspeed": windspeed
            }
        ])
        
        with st.spinner("Calculating estimate..."):
            try:
                preds = predict(model, input_data)
                prediction_val = float(preds[0])
                
                st.markdown(
                    f"""
                    <div style="background: linear-gradient(90deg, #115e59, #14b8a6); padding: 2rem; border-radius: 1rem; text-align: center; margin-top: 1.5rem; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);">
                        <h3 style="color: #ccfbf1; margin: 0; font-family: sans-serif; font-size: 1.25rem; font-weight: 500;">Estimated Rental Demand</h3>
                        <h1 style="color: white; margin: 0.5rem 0 0; font-family: sans-serif; font-size: 3.5rem; font-weight: 800;">{prediction_val:,.0f} <span style="font-size: 1.5rem; font-weight: 400;">bikes</span></h1>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"Prediction failed: {e}", icon=":material/error:")
