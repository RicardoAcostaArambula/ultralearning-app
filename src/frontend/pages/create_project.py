import streamlit as st
import requests
from pages import auth_and_sidebar_setup
from datetime import date
API_URL = "http://127.0.0.1:8000"

auth_and_sidebar_setup()
st.write("Create new Ultralearning project")
title = st.text_input("📝 Project Title")
goal = st.text_input("🎯 Project Goal")
generate_outline = st.checkbox("Generate outline.")
upload_outline = st.checkbox("Write outline")
deadline = st.date_input("📅 Project deadline", format="YYYY-MM-DD")
user_id = st.session_state['id']
submit = st.button("Create Project")
prompt = f''' You are now my mentor and I am writing an outline for an ultralearning 
            project with the following goal {goal}. The deadline is {deadline}. Provide
            an outline with everything I need to archieve the goal previously mention by 
            the deadline provided. Please provide the outline in the following format:
            1. outline item one - week 1.
                1.1 Exercise 
            2. outline item two - week 2.
                2.1 Exercise 
            n. outline item n - week n
                n.1 Exercise 
            The exercises need to reforce the outline item using open ended exercises and
            the number of exercises need to be enough to attack the topic from every angle
            to reach mastery. As you see relevant provide quizzes and exams.
          '''
if submit:
    project = {
        "title": title,
        "goal": goal,
        "deadline": deadline.isoformat(),
        "user_id": user_id
    }
    existing_project = requests.get(f"{API_URL}/projects/{title}", params={'project_name': title, 'user_id' : int(st.session_state['id'])}).status_code == 200 
    if title == "" or title == None or goal == None or title.strip() == "":
        st.error("Please Enter a valid name")
    elif existing_project:
        st.error("Please, select another name")
    else:
        response = requests.post(f"{API_URL}/projects",json=project)
        if response.status_code ==200:
            st.success(f"✅Project {title}, created successfully!")
        else:
            st.error(f"❌ Error: {response.status_code}")
            try: 
                st.error(response.json().get("details"))
            except:
                st.write("Could not decode error response.")
