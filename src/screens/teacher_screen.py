
import streamlit as st

from src.components.header import header_dashboard
from src.components.footer import footer


def teacher_screen():

    # Page configuration
    st.markdown("""
        <style>
            .teacher-welcome {
                color: #1F2937 !important;
                font-size: 32px !important;
                font-weight: 800 !important;
                text-align: center !important;
                margin-top: 15px !important;
                margin-bottom: 20px !important;
            }

            .teacher-subtitle {
                color: #475569 !important;
                font-size: 16px !important;
                text-align: center !important;
                margin-bottom: 25px !important;
            }

            div.stButton > button {
                border-radius: 30px !important;
                min-height: 45px !important;
                font-weight: 600 !important;
            }

            .teacher-section-title {
                color: #111827 !important;
                font-size: 32px !important;
                font-weight: 900 !important;
                margin-top: 30px !important;
                margin-bottom: 20px !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # Header
    header_dashboard()

    # Get teacher name from session
    teacher_name = st.session_state.get("teacher_name", "Teacher")

    # Welcome section
    st.markdown(
        f'<div class="teacher-welcome">Welcome, {teacher_name}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="teacher-subtitle">Teacher Dashboard</div>',
        unsafe_allow_html=True
    )

    # Logout button
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button("Logout ⌘ + Backspace", use_container_width=True):
            st.session_state.clear()
            st.rerun()

    st.markdown("---")

    # Dashboard navigation
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📸 Take Attendance", use_container_width=True):
            st.session_state["teacher_page"] = "attendance"

    with col2:
        if st.button("📚 Manage Subjects", use_container_width=True):
            st.session_state["teacher_page"] = "subjects"

    with col3:
        if st.button("📊 Attendance Records", use_container_width=True):
            st.session_state["teacher_page"] = "records"

    # Main dashboard content
    st.markdown(
        '<div class="teacher-section-title">Teacher Dashboard</div>',
        unsafe_allow_html=True
    )

    st.info("Welcome to your teacher dashboard. Select an option above to continue.")

    # Footer
    footer()
