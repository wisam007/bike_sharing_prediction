import streamlit as st
from config import FIGURE_DIR

st.header("Exploratory data analysis")
st.write(
    "Select a chart below to visualize dataset trends, distributions, "
    "outliers, and feature correlations generated during training."
)

st.space("medium")

plot_options = {
    "Rental distribution": ("distribution_of_cnt.png", "Shows the overall distribution profile of the total daily bike rentals target variable."),
    "Numerical Feature distributions": ("eda_distributions.png", "Density distributions with kernel density estimation curves for temperature, humidity, windspeed, and rentals."),
    "Categorical Feature Distribution":("categorical_distributions.png", "Distribution of categorical features which are season,mnth,weekday (0 = No,1 = Yes),weathersit,yr(0 = 2018,1 = 2019),workingday,holiday"),
    "Weather outliers": ("weather_outlier_subplots.png", "Boxplots revealing weather and rental demand outliers."),
    "Categorical variations": ("eda_boxplots_categorical.png", "Analysis of rental demand variations across seasons, months, weekdays, and weather situations."),
    "Correlation matrix": ("eda_correlation_heatmap.png", "Pearson correlation matrix for numerical features and rental counts."),
    "Feature scatterplots": ("eda_scatterplots.png", "Bivariate distributions mapping temperature, humidity, and windspeed directly against rental count.")
}

selection = st.segmented_control(
    "Select visualization to display",
    options=list(plot_options.keys()),
    default="Rental distribution"
)

if selection:
    filename, caption = plot_options[selection]
    path = FIGURE_DIR / filename
    
    if path.exists():
        with st.container(border=True):
            st.image(str(path))
            st.caption(f"{caption} (Saved figure: reports/figures/{filename})")
    else:
        st.warning(f"Plot figure not found: {filename}", icon=":material/warning:")
