import streamlit as st
import json
from config import JSON_DIR

st.header("Feature importance")

best_model_path = JSON_DIR / "best_model.json"

if best_model_path.exists():
    with open(best_model_path, "r") as f:
        best_model = json.load(f)
    best_model_name = best_model.get("Model", "Unknown")
else:
    best_model_name = "Support Vector Regressor"

st.write(
    f"The currently selected champion model is **{best_model_name}**."
)

with st.container(border=True):
    st.markdown("#### :material/info: Model feature interpretation")
    st.write(
        "For non-linear models like **Support Vector Regressors (SVR)** with RBF kernels, "
        "feature importances are not directly calculated as simple coefficients or split counts. "
        "Instead, the model operates on support vectors in high-dimensional space. "
        "However, correlation analysis and tree-based model reports suggest the following feature impacts:"
    )

    st.markdown(
        "- **Strong positive predictors**: Temperature (`temp`) has the highest correlation with bike rentals. Demand rises as the temperature becomes warmer (until it gets too hot).\n"
        "- **Temporal indicators**: Year (`yr`) shows a significant positive impact, reflecting year-over-year growth in bike sharing system adoption.\n"
        "- **Negative predictors**: High humidity (`hum`) and wind speed (`windspeed`) negatively impact rental counts, as they represent less pleasant riding conditions.\n"
        "- **Weather conditions**: Clear weather (`weathersit = clear`) increases demand, while rainy or snowy weather (`weathersit = light_rain_snow`) strongly suppresses rentals."
    )

st.space("medium")

with st.container(border=True):
    st.markdown("#### :material/pipeline: Feature types in ML pipeline")
    cols = st.columns(3)
    with cols[0]:
        st.markdown("**Numerical (Scaled)**")
        st.caption("Numerical values normalized to zero-mean and unit variance:")
        st.write("- Temperature (`temp`)\n- Humidity (`hum`)\n- Wind speed (`windspeed`)")
    with cols[1]:
        st.markdown("**Categorical (One-Hot Encoded)**")
        st.caption("Categorical variables converted to one-hot columns (excluding first):")
        st.write("- Season (`season`)\n- Month (`mnth`)\n- Weather situation (`weathersit`)\n- Weekday (`weekday`)")
    with cols[2]:
        st.markdown("**Passthrough (As-Is)**")
        st.caption("Binary features passed directly to the model:")
        st.write("- Year (`yr`)\n- Holiday (`holiday`)\n- Working day (`workingday`)")
