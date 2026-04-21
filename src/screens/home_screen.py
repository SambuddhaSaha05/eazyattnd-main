import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
 
    header_home()
    style_background_home()
    style_base_layout()


    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I am Student")
        st.image("https://cdn-icons-png.freepik.com/512/17360/17360019.png?ga=GA1.1.1884972210.1776713752", width=120)
        if st.button("Student Portal  ↗", type="tertiary"):
            st.session_state['login_type'] = 'student'
            st.rerun()
       
    with col2:
       st.header("I am Teacher")
       st.image("https://cdn-icons-png.freepik.com/512/13402/13402695.png?ga=GA1.1.1884972210.1776713752", width=120)
       if st.button("Teacher Portal  ↗", type="tertiary"):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()



