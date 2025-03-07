import streamlit as st

def initialize_session_state():
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'
    if 'students' not in st.session_state:
        st.session_state.students = {}
    if 'current_student' not in st.session_state:
        st.session_state.current_student = None 