import streamlit as st
import requests
API_URL = "http://127.0.0.1:8000"
st.set_page_config(initial_sidebar_state="collapsed")
st.sidebar.page_link('login.py', label = "Log in")
with st.container():
    st.header("Welcome to Ultralearning!")
    with st.form("login_form", clear_on_submit=False):
        row_input = st.columns([2, 1])
        username = row_input[0].text_input("Username")
        password = row_input[0].text_input("Password", type= "password")

        col1, col2, _ = st.columns([2, 2, 1])
        with col1: 
            submit = st.form_submit_button("Log in", type="primary")
        with col2: 
            create_account = st.form_submit_button("Create Account")
            # if create_account:
            #    st.switch_page("pages/create_account.py")

    if submit and (username == "" or password == ""):
        st.error("Please enter your username and password.")
    elif submit:
        response = requests.get(f"{API_URL}/users/{username}", json=username) 
        if response.status_code == 200:
            user = response.json()
            if password == user['password']:
                #sucess move to homepage
                st.session_state['logged'] = True
                st.session_state['username'] = user['username']
                st.session_state['id'] = user['id']
                st.switch_page("pages/menu.py")
            else:
                #prompt user to try again 
                st.error("Wrong password, please try again.")
        else:
            st.write("User not found, please try again")
    elif create_account:
        st.write("You will be redirected to create a new account:')'")
    elif create_account:
        st.switch_page("pages/create_account.py")
