import streamlit as st 
import requests 
from pages import auth_and_sidebar_setup 
API_URL = "http://127.0.0.1:8000" 
auth_and_sidebar_setup()
st.subheader(f"Title: {st.session_state['project']['title']}")
st.subheader(f"Goal: {st.session_state['project']['goal']}")
st.subheader(f"Deadline:{st.session_state['project']['deadline']}")
