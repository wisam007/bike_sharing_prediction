import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Project Report", page_icon="📝")

st.title("Project Report")

for path in [
    Path("reports/eda_report.md"),
    Path("reports/model_report.md"),
    Path("reports/evaluation_report.md"),
    Path("reports/project_summary.md"),
]:
    if path.exists():
        st.subheader(path.stem.replace("_", " ").title())
        st.markdown(path.read_text(encoding="utf-8"))
        st.divider()
    else:
        st.info(f"Report not generated yet: {path}")
