import streamlit as st
import requests
from pages import auth_and_sidebar_setup
API_URL = "http://127.0.0.1:8000"
auth_and_sidebar_setup()
user_id = st.session_state['id']
response = requests.get(f"{API_URL}/projects", params={"user_id": user_id})
if response.status_code == 200:
    projects = response.json()
    number = 1
    for project in projects:
        st.subheader(f"{number} {project['title']}")
        st.write(f"Goal: {project['goal']}")
        st.write(f"Deadline: {project['deadline']}")
        number+=1
else:
    st.error(f"Error: {response.json().get('detail')}")
