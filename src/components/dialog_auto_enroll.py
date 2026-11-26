import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase

import time


@st.dialog("Quick Enrollment")
def auto_enroll_dialog(subject_code):
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

        /* Headings, markdown, and bold subject name inside modal */
        div[role="dialog"] h1,
        div[role="dialog"] h2,
        div[role="dialog"] h3,
        div[role="dialog"] p,
        div[role="dialog"] span,
        div[role="dialog"] strong,
        div[role="dialog"] label {
            color: #0F172A !important;
        }

        /* Primary button (Yes enroll now!) - Deep Indigo Gradient */
        div[role="dialog"] button[data-testid="stBaseButton-primary"],
        div[role="dialog"] button[kind="primary"] {
            background: linear-gradient(135deg, #4338CA 0%, #2563EB 100%) !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
        }

        /* Secondary/default buttons (Close, Got it!, No thanks) - Crisp Rose */
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

        /* Alerts (Error, Info, Success) inside modal */
        div[role="dialog"] div[data-testid="stAlert"] {
            background-color: #F8FAFC !important;
            border: 1.5px solid #CBD5E1 !important;
            border-radius: 12px !important;
        }

        div[role="dialog"] div[data-testid="stAlert"] p,
        div[role="dialog"] div[data-testid="stAlert"] span {
            color: #0F172A !important;
            font-weight: 500 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    student_id = st.session_state.student_data['student_id']

    res = supabase.table('subjects').select('subject_id, name').eq('subject_code', subject_code).execute()
    if not res.data:
        st.error('Subject Code not found!')
        if st.button('Close'):
            st.query_params.clear()
            st.rerun()
        return
    subject = res.data[0]

    check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
    if check.data:
        st.info('Youre already enrolled!')
        if st.button('Got it!'):
            st.query_params.clear()
            st.rerun()
        return
    st.markdown(f'Would you like to enroll in **{subject["name"]}**?')

    col1, col2 = st.columns(2)

    with col1:
        if st.button('No thanks'):
            st.query_params.clear()
            st.rerun()
    with col2:
        if st.button('Yes enroll now!', type='primary', width='stretch'):
            enroll_student_to_subject(student_id, subject['subject_id'])
            st.success('Joined succesfully!')
            st.query_params.clear()
            time.sleep(2)
            st.rerun()
