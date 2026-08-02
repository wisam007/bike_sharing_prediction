import streamlit as st

st.header("Team members")
st.write("Meet the team responsible for modularizing and delivering this project.")

st.space("medium")

team_members = [
    {
        "name": "Wissam Jemal",
        "role": "Machine Learning Engineer",
        "focus": "Model development, pipelining, and frontend deployment",
        "icon": ":material/engineering:"
    },
    {
        "name": "Yasmin Anwar",
        "role": "Data Scientist",
        "focus": "Exploratory analysis, data cleaning, and feature engineering",
        "icon": ":material/analytics:"
    },
    {
        "name": "Betelhem ",
        "role": "Product Analyst",
        "focus": "Business problem framing, evaluation criteria, and reporting",
        "icon": ":material/assignment_ind:"
    },
]

cols = st.columns(3)

for idx, member in enumerate(team_members):
    with cols[idx].container(border=True, height="stretch"):
        st.markdown(f"### {member['icon']} {member['name']}")
        st.markdown(f"**{member['role']}**")
        st.caption(member["focus"])
