import streamlit as st
from config import FIGURE_DIR


st.header("Residual analysis")
st.write(
    "Residual diagnostics measure the difference between actual and predicted bike rental counts. "
    "Analyzing residuals helps verify regression assumptions such as constant variance (homoscedasticity) "
    "and normal distribution of errors."
)

st.space("medium")

with st.container(border=True):
    st.markdown("#### :material/monitoring: Key diagnostic concepts")
    st.write(
        "Residuals are defined as: $e_i = y_i - \\hat{y}_i$\n"
        "- **Mean residual**: Should be close to 0. A non-zero mean indicates systematic bias.\n"
        "- **Normality**: Residuals should ideally follow a normal distribution. If they are skewed, the model may be missing key non-linear terms or interaction effects.\n"
        "- **Heteroscedasticity**: The spread of residuals should be constant across the range of predicted values. If residuals fan out or curve, it suggests non-constant variance."
    )

st.space("medium")

plot_options = {
    "1. Actual vs. Predicted": ("actual_vs_predicted.png", "PlotUnderprediction at High Values: The model fails to capture high bike rental counts. When actual rentals exceed 7,000, the predictions flatten out near 6,500.Moderate Linear Fit: For mid-range rental counts (2,000 to 6,000), the data points roughly follow the diagonal reference line, showing a decent linear relationship."),
    "2. Residual Distribution Plot": ("residual_distribution.png", "Slight Left Skew: The error distribution is roughly bell-shaped but exhibits a longer tail on the negative side (down to -2,000).Violation of Normality: Because of the left skew, the assumption of perfectly normally distributed residuals is slightly violated."),
    "3. Residuals vs. Predictions Plot":("residual_plot.png", "The spread of the residuals is not constant. Errors are tightly packed for predictions below 2,000 but expand significantly between 3,000 and 5,000."),
   }

selection = st.segmented_control(
    "Select visualization to display",
    options=list(plot_options.keys()),
    default="1. Actual vs. Predicted"
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
