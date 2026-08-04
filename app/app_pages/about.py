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
│       ├── loader.py │
|       ├── preprocessing.py 
│       ├── features.py 
│       ├── modeling.py
│       ├── evaluation.py
│       ├── visualization.py 
│       ├── reporting.py
│       ├── persistence.py
│       ├── inference.py 
|       └── eda.py
├── config.py 
├── main.py               # Main pipeline script
├── predict.py 
├── requirements.txt 
└── README.md
        """,
        language="text"
    )
import streamlit as st

st.header("Team members")
st.write("Meet the team responsible for modularizing and delivering this project.")

st.space("medium")

team_members = [
    {
        "name": "Wissam Jemal",
        "icon": ":material/engineering:"
    },
    {
        "name": "Yasmin Anwar",
        "icon": ":material/analytics:"
    },
    {
        "name": "Betelhem Mulat",
        "icon": ":material/assignment_ind:"
    },
]

cols = st.columns(3)

for idx, member in enumerate(team_members):
    with cols[idx].container(border=True, height="stretch"):
        st.markdown(f"### {member['icon']} {member['name']}")
        

