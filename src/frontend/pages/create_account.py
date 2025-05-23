import streamlit as st
import requests
import time
API_URL = "http://127.0.0.1:8000"
st.set_page_config(initial_sidebar_state="collapsed")
with st.container():
    st.header("Create New Account")
    new_username = st.text_input("New username", key="new_username")
    password_attempt_one = st.text_input("Password", type = "password", key="password_one")
    password_attempt_two = st.text_input("Confirm password", type = "password", key="password_two")
    create_account = st.button("Create New Account", type="primary")
if create_account: 
    db_user = requests.get(f"{API_URL}/users/{new_username}")
    if password_attempt_one != password_attempt_two:
        st.error("Passwords do not match.")
        #may rerun
    elif db_user.status_code==200:
        st.error("Username already exist.")
        #may rerun
    else:
        #create new user in database
        new_account = {
            'username': new_username,
            'password':  password_attempt_one
        }
        response = requests.post(f"{API_URL}/users", json = new_account)
        if response.status_code == 200:
            st.success(f"✅Account '{new_username}' created successfully!\n Redirecting...")
            time.sleep(4)
            st.switch_page("login.py")
