import streamlit as st

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

st.info(
    "Residual diagnostic visualizations and metric logs are generated as part of the automated training run "
    "and are saved in the `reports/` folder.",
    icon=":material/info:"
)
