import streamlit as st
from pathlib import Path

from config.config import PLOTS_DIR

st.set_page_config(page_title="EDA", page_icon="📈")

st.title("Exploratory Data Analysis")

plot_files = [
    ("Distribution of Bike Rentals", PLOTS_DIR / "histogram_cnt.png"),
    ("Correlation Heatmap", PLOTS_DIR / "correlation_heatmap.png"),
    ("Weather Feature Boxplots", PLOTS_DIR / "boxplot_weather.png"),
    ("Temperature vs Rental Count", PLOTS_DIR / "scatter_temp_cnt.png"),
]

for title, path in plot_files:
    if path.exists():
        st.subheader(title)
        st.image(str(path), use_container_width=True)
        st.caption("Saved plot from the modularized notebook workflow.")
    else:
        st.info(f"Plot not generated yet: {path.name}")
