import streamlit as st
def auth_and_sidebar_setup():
    if 'logged' not in st.session_state or not st.session_state['logged']:
        st.switch_page('login.py')
    st.sidebar.page_link('pages/menu.py', label='home')
    st.sidebar.page_link('pages/create_project.py', label='create new project')
    st.sidebar.page_link('pages/project_main.py', label='project main page')
    st.sidebar.page_link('pages/projects.py', label='projects')
