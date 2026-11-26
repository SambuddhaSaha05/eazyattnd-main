import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

from src.database.db import create_attendance


def show_attendance_result(df, logs):
    st.markdown("""
    <style>
        /* Crisp white modal surface */
        div[role="dialog"],
        div[data-testid="stDialog"] div[role="dialog"] {
            background-color: #FFFFFF !important;
            color: #0F172A !important;
            border: 1.5px solid #CBD5E1 !important;
            border-radius: 18px !important;
        }

        /* Headings & body text inside modal */
        div[role="dialog"] h1,
        div[role="dialog"] h2,
        div[role="dialog"] h3,
        div[role="dialog"] p,
        div[role="dialog"] span,
        div[role="dialog"] label {
            color: #0F172A !important;
        }

        /* Dataframe container */
        div[role="dialog"] div[data-testid="stDataFrame"] {
            background-color: #FFFFFF !important;
            border: 1.5px solid #CBD5E1 !important;
            border-radius: 12px !important;
            padding: 0.35rem !important;
            color: #0F172A !important;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05) !important;
        }

        /* Primary button (Confirm & Save) - Deep Indigo Gradient */
        div[role="dialog"] button[data-testid="stBaseButton-primary"],
        div[role="dialog"] button[kind="primary"] {
            background: linear-gradient(135deg, #4338CA 0%, #2563EB 100%) !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
        }

        /* Secondary/default button (Discard) - Crisp Rose */
        div[role="dialog"] button[data-testid="stBaseButton-secondary"],
        div[role="dialog"] button[kind="secondary"] {
            background-color: #E11D48 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 10px rgba(225, 29, 72, 0.22) !important;
        }

        /* Keep white text strictly inside action buttons */
        div[role="dialog"] button[data-testid="stBaseButton-primary"] p,
        div[role="dialog"] button[data-testid="stBaseButton-primary"] span,
        div[role="dialog"] button[kind="primary"] p,
        div[role="dialog"] button[kind="primary"] span,
        div[role="dialog"] button[data-testid="stBaseButton-secondary"] p,
        div[role="dialog"] button[data-testid="stBaseButton-secondary"] span,
        div[role="dialog"] button[kind="secondary"] p,
        div[role="dialog"] button[kind="secondary"] span {
            color: #FFFFFF !important;
        }

        /* Alerts inside modal */
        div[role="dialog"] div[data-testid="stAlert"] {
            background-color: #FEF2F2 !important;
            border: 1px solid #FECACA !important;
            border-radius: 10px !important;
        }

        div[role="dialog"] div[data-testid="stAlert"] p {
            color: #991B1B !important;
            font-weight: 500 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    st.write('Please review attendance before confirming.')
    st.dataframe(df, hide_index=True, width='stretch')

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Discard', width='stretch'):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button('Confirm & Save', width='stretch', type='primary'):
            try:
                create_attendance(logs)
                st.toast("Attendance taken")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                st.rerun()
            except Exception as e:
                st.error('Sync failed!')


@st.dialog("Attendance Reports")
def attendance_result_dialog(df, logs):
    show_attendance_result(df, logs)
