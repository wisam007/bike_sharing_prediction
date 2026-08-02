import streamlit as st

st.header("About project")
st.write(
    "This repository demonstrates how to modularize an experimental Jupyter notebook into a clean, "
    "maintainable production codebase. All business logic, preprocessing, evaluation, and visualizations "
    "are isolated into structured Python modules, while the Streamlit app acts as a thin frontend layer."
)

st.space("medium")

with st.container(border=True):
    st.markdown("#### :material/folder_open: Codebase structure")
    st.code(
        """
├── app/                  # Streamlit application
│   ├── app.py            # Entrypoint & navigation hub
│   └── app_pages/        # Modular page scripts
├── data/                 # Raw and processed datasets
├── model/                # Persisted pipeline models (.pkl)
├── reports/              # Generated markdown, tables, and charts
│   ├── figures/          # EDA plots
│   ├── json/             # Evaluation metrics
│   └── tables/           # Statistics CSVs
├── src/                  # Core modular package
│   ├── features.py       # Pipelines & data transformers
│   ├── modeling.py       # Model training algorithms
│   ├── persistence.py    # Joblib load/save utils
│   ├── preprocessing.py  # Data cleaning & data quality checks
│   └── loader.py         # Dataset read utils
└── main.py               # Main pipeline script
        """,
        language="text"
    )
