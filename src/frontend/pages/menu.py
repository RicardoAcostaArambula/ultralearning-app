from requests.api import get
import streamlit as st 
from streamlit.runtime.state import session_state 
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
        response = requests.get(f"{API_URL}/projects/{project_name}", params={'project_name': project_name, 'user_id' : st.session_state['id']})
        if response.status_code == 200:
            st.session_state['project_loaded'] = True
            st.session_state['project'] = response.json()
        else:
            st.session_state['load_error'] = True
            st.session_state['load_error_message'] = f"Error: {response.json().get('detail')}"

    st.text_input("Write the Project's Name: ", key="user_project_name_input", on_change=get_project)
    if st.session_state.get('project_loaded'):
        st.session_state['project_loaded'] = False 
        st.write("Openning file...")
        time.sleep(1)
        st.switch_page("pages/project_main.py")
    if st.session_state.get('load_error'):
        st.session_state['load_error'] = False 
        st.error(st.session_state['load_error_message'])
        
with st.container(border=True): 
    st.header("Ultralearning Menu")
    if st.button("Create project"):
        st.switch_page('pages/create_project.py') 
    elif st.button("Open project"):
        open_project() 
    elif st.button("See all projects"):
        st.switch_page('pages/projects.py') 
