import os
import sys
from pathlib import Path

# Add the project root to sys.path so sub-pages can import config and src modules
root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

import streamlit as st

st.set_page_config(
    page_title="Bike Sharing Demand Prediction",
    page_icon=":material/directions_bike:",
    layout="wide"
)

# Define pages in groups relative to app.py location
pages = {
    "Overview": [
        st.Page("app_pages/home.py", title="Home", icon=":material/home:"),
        st.Page("app_pages/project.py", title="Project description", icon=":material/info:"),
        st.Page("app_pages/about.py", title="About project", icon=":material/description:"),
        st.Page("app_pages/team.py", title="Team members", icon=":material/group:"),
    ],
    "Data Exploration": [
        st.Page("app_pages/dataset.py", title="Dataset information", icon=":material/database:"),
        st.Page("app_pages/eda.py", title="Exploratory data analysis", icon=":material/analytics:"),
    ],
    "Model & Performance": [
        st.Page("app_pages/feature_importance.py", title="Feature importance", icon=":material/explore:"),
        st.Page("app_pages/model.py", title="Model training info", icon=":material/memory:"),
        st.Page("app_pages/residual_analysis.py", title="Residual analysis", icon=":material/query_stats:"),
    ],
    "Inference": [
        st.Page("app_pages/prediction.py", title="Prediction portal", icon=":material/online_prediction:"),
    ]
}

# Run navigation
page = st.navigation(pages, position="sidebar")

# Run selected page script
page.run()
