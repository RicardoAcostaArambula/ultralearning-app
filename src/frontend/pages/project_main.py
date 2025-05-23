import streamlit as st 
import requests 
from pages import auth_and_sidebar_setup 
import time
API_URL = "http://127.0.0.1:8000" 
auth_and_sidebar_setup()
if 'project' not in st.session_state:
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
    open_project()
else:
    st.subheader(f"Title: {st.session_state['project']['title']}")
    st.subheader(f"Goal: {st.session_state['project']['goal']}")
    st.subheader(f"Deadline:{st.session_state['project']['deadline']}")
    st.subheader(f"Next steps: ")
