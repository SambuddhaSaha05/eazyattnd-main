import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase

import time


@st.dialog("Enroll in Subject")
def enroll_dialog():
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

        /* Headings, text, and widget labels inside modal */
        div[role="dialog"] h1,
        div[role="dialog"] h2,
        div[role="dialog"] h3,
        div[role="dialog"] p,
        div[role="dialog"] span,
        div[role="dialog"] label {
            color: #0F172A !important;
        }

        div[role="dialog"] div[data-testid="stWidgetLabel"] p,
        div[role="dialog"] div[data-testid="stWidgetLabel"] label {
            color: #0F172A !important;
            font-weight: 600 !important;
        }

        /* Text input */
        div[role="dialog"] input,
        div[role="dialog"] textarea {
            background-color: #FFFFFF !important;
            color: #0F172A !important;
            -webkit-text-fill-color: #0F172A !important;
            border: 1.5px solid #94A3B8 !important;
            border-radius: 10px !important;
        }

        div[role="dialog"] input:focus,
        div[role="dialog"] textarea:focus {
            border-color: #4338CA !important;
            box-shadow: 0 0 0 3px rgba(67, 56, 202, 0.18) !important;
        }

        div[role="dialog"] input::placeholder,
        div[role="dialog"] textarea::placeholder {
            color: #64748B !important;
            opacity: 1 !important;
            -webkit-text-fill-color: #64748B !important;
        }

        /* Primary button (Enroll now) - Deep Indigo Gradient */
        div[role="dialog"] button[data-testid="stBaseButton-primary"],
        div[role="dialog"] button[kind="primary"] {
            background: linear-gradient(135deg, #4338CA 0%, #2563EB 100%) !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
        }

        div[role="dialog"] button[data-testid="stBaseButton-primary"] p,
        div[role="dialog"] button[data-testid="stBaseButton-primary"] span,
        div[role="dialog"] button[kind="primary"] p,
        div[role="dialog"] button[kind="primary"] span {
            color: #FFFFFF !important;
        }

        /* Alerts (Warning, Success) inside modal */
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

    st.write('Enter the subject code provided by your teacher to enroll')
    join_code = st.text_input('Subject Code', placeholder='Eg. CS101')

    if st.button('Enroll now', type='primary', width='stretch'):
        if join_code:
            res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', join_code).execute()
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data['student_id']

                check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
                if check.data:
                    st.warning('You are already enrolled in this program')
                else:
                    enroll_student_to_subject(student_id, subject['subject_id'])
                    st.success('Succesfully enrolled!')
                    time.sleep(1)
                    st.rerun()
        else:
            st.warning('Please enter a subject code')
