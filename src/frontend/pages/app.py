import streamlit as st
import requests
from datetime import date
API_URL = "http://127.0.0.1:8000"

if 'logged' not in st.session_state or not st.session_state['logged']:
    st.switch_page('login.py')
st.sidebar.page_link('pages/app.py', label='Home')

st.title("Welcome to Ultralearning!")
col1, col2 = st.columns(2, border=True)
with col1:
    with st.form("create_project_form", border=False):
        st.write("Create new Ultralearning project")
        title = st.text_input("📝 Project Title")
        goal = st.text_input("🎯 Project Goal")
        deadline = st.date_input("📅 Project deadline", format="YYYY-MM-DD")
        user_id = st.number_input("👤 Enter User ID", min_value=0, value=0, key="user_id_project_creation")
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
with col2: 
    user_id = st.number_input("Enter User ID", min_value=0, value=0, key="user_id_get_project")
    if st.button("Fetch Projects"):
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

