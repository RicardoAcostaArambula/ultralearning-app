import streamlit as st
import requests
from pages import auth_and_sidebar_setup
from datetime import date
API_URL = "http://127.0.0.1:8000"

auth_and_sidebar_setup()
with st.form("create_project_form", border=False):
    st.write("Create new Ultralearning project")
    title = st.text_input("📝 Project Title")
    goal = st.text_input("🎯 Project Goal")
    deadline = st.date_input("📅 Project deadline", format="YYYY-MM-DD")
    user_id = st.session_state['id']
    submit = st.form_submit_button("Create Project")
    if submit:
        project = {
            "title": title,
            "goal": goal,
            "deadline": deadline.isoformat(),
            "user_id": user_id
        }
        response = requests.post(f"{API_URL}/projects",json=project)
        if response.status_code ==200:
            st.success(f"✅Project {title}, created successfully!")
        else:
            st.error(f"❌ Error: {response.status_code}")
            try: 
                st.error(response.json().get("details"))
            except:
                st.write("Could not decode error response.")
