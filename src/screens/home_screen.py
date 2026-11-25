import streamlit as st

from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    # Apply styling first
    style_background_home()
    style_base_layout()

    # Header
    header_home()

    st.space()

    # Portal layout
    col1, col2 = st.columns([1, 1], gap="large")

    # Student Portal
    with col1:
        st.header("I am Student", text_alignment="center")

        st.image(
            "https://cdn-icons-png.freepik.com/512/17360/17360019.png?ga=GA1.1.1884972210.1776713752",
            width=120,
        )

        st.space()

        if st.button(
            "Student Portal ↗",
            type="tertiary",
            width="stretch",
        ):
            st.session_state["login_type"] = "student"
            st.rerun()

    # Teacher Portal
    with col2:
        st.header("I am Teacher", text_alignment="center")

        st.image(
            "https://cdn-icons-png.freepik.com/512/13402/13402695.png?ga=GA1.1.1884972210.1776713752",
            width=120,
        )

        st.space()

        if st.button(
            "Teacher Portal ↗",
            type="tertiary",
            width="stretch",
        ):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    st.space()

    # Footer
    footer_home()
