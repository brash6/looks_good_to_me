import os
import streamlit as st
from openai import OpenAI

from package_review import get_file_content, get_package_review

st.set_page_config(
    page_title="Looks Good To Me",
    page_icon="🧊")

ss = st.session_state

st.title("# Looks Good To Me")
st.write('## 1- Enter your OpenAI API key')
api_key = st.text_input('OpenAI API key', type='password', key="api_key",
                        label_visibility="collapsed")

# Getting secret API
OPEN_AI_KEY = ss.get('api_key')
client = OpenAI(api_key=OPEN_AI_KEY)

t1, t2 = st.tabs(['Review package structure', 'Review a specific file'])

with t1:
    # Reviewing package structure
    st.title("Python Package Structure Review")
    repo_url_1 = st.text_input("Enter GitHub repository URL", key="1")
    branch_to_review = st.text_input(
        "Enter the name of the branch you want to review", key="2")

    if st.button("Review Package"):
        try:
            review_struc = get_package_review(
                repo_url_1, branch_to_review, client)
            st.write(review_struc)
        except Exception as error:
            st.write(error)

with t2:
    # Reviewing a specific file
    st.title("Python File Review")
    repo_url_2 = st.text_input("Enter GitHub repository URL", key="3")
    file_path = st.text_input(
        "Enter the path of the python file you want to review", key="4")

    if st.button("Review File"):
        try:
            review_file = get_file_content(repo_url_2, file_path, client)
            st.write(review_file)
        except Exception as error:
            st.write(error)
