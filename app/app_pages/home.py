import streamlit as st

st.markdown(
    """
    <div style="background: linear-gradient(90deg, #0f172a, #14b8a6); padding: 2.5rem; border-radius: 1rem; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0; font-family: sans-serif; font-size: 2.5rem; font-weight: 700;">Bike Sharing Demand Prediction</h1>
        <p style="color: #ccfbf1; margin-top: 0.75rem; font-family: sans-serif; font-size: 1.1rem;">A production-style modular machine learning system for forecasting daily bike rentals.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("### Welcome to the analytics portal")
st.write(
    "This interactive dashboard is the frontend for a robust, modularized machine learning workflow. "
    "It demonstrates how exploratory notebook experiments can be transitioned into structured, clean Python code."
)

st.space("medium")

with st.container(border=True):
    st.markdown("#### :material/map: Navigation guide")
    st.write(
        "Use the sidebar to explore the application sections:"
    )
    cols = st.columns(3)
    with cols[0]:
        st.markdown("**Overview**")
        st.caption("Learn about the business problem, context, and project goals.")
    with cols[1]:
        st.markdown("**Data & EDA**")
        st.caption("Inspect raw data statistics and review visual patterns from analysis.")
    with cols[2]:
        st.markdown("**Model & Prediction**")
        st.caption("Compare algorithms, view importance, and make real-time predictions.")
