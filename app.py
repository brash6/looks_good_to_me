import streamlit as st
from openai import OpenAI

from package_review import get_file_content, get_package_review

st.write('# Looks good to me')
st.write('## 1- Enter your OpenAI API key')
api_key = st.text_input('OpenAI API key', type='password',
                        label_visibility="collapsed")

client = OpenAI(api_key=api_key)

t1, t2 = st.tabs(['Review package structure', 'Review a specific file'])

with t1:
    # Title and input field for GitHub repository URL
    st.title("Python Package Structure Review")
    repo_url_1 = st.text_input("Enter GitHub repository URL", key="1")
    branch_to_review = st.text_input(
        "Enter the name of the branch you want to review", key="2")

    # Button to trigger review
    if st.button("Review Package"):
        # Call backend function to retrieve and display review
        review_struc = get_package_review(repo_url_1, branch_to_review, client)
        st.write(review_struc)

with t2:

    # Title and input field for GitHub repository URL
    st.title("Python File Review")
    repo_url_2 = st.text_input("Enter GitHub repository URL", key="3")
    file_path = st.text_input(
        "Enter the path of the python file you want to review", key="4")

    # Button to trigger review
    if st.button("Review File"):
        # Call backend function to retrieve and display review
        review_file = get_file_content(repo_url_2, file_path, client)
        st.write(review_file)
