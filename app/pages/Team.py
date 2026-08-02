import streamlit as st

st.set_page_config(page_title="Team", page_icon="👥")

st.title("Team Members")

team_members = [
    {"name": "Alex Morgan", "role": "ML Engineer", "focus": "Model development and deployment"},
    {"name": "Jamie Carter", "role": "Data Scientist", "focus": "Feature engineering and experimentation"},
    {"name": "Taylor Lee", "role": "Product Analyst", "focus": "Business problem framing and evaluation"},
]

for member in team_members:
    with st.container():
        st.subheader(member["name"])
        st.write(member["role"])
        st.caption(member["focus"])
        st.write("")
