import streamlit as st
from pages import auth_and_sidebar_setup
import requests 
import time

API_URL = "http://127.0.0.1:8000"
auth_and_sidebar_setup()
@st.dialog("Open Project")
def open_project():
    #function fetches project
    def get_project():
        project_name = st.session_state['user_project_name_input'] 
        response = requests.get(f"{API_URL}/projects/{project_name}", params={'project_name': project_name})
        if response.status_code == 200:
            st.session_state['project'] = response.json()
        else:
            st.error(f"Error: {response.json().get('detail')}")
    st.text_input("Write the Project's Name: ", key="user_project_name_input", on_change=get_project)
    if 'project' in st.session_state:
        st.write("Openning file...")
        time.sleep(1)
        st.switch_page("pages/project_main.py")

with st.container(border=True): 
    st.header("Ultralearning Menu")
    if st.button("Create project"):
        st.switch_page('pages/create_project.py') 
    elif st.button("Open project"):
       open_project() 
    elif st.button("See all projects"):
        st.switch_page('pages/projects.py') 
