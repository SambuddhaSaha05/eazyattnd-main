import streamlit as st
from src.database.db import create_subject


@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
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

        /* Text inputs */
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

        /* Primary button (Create Subject Now) - Deep Indigo Gradient */
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

        /* Alerts (Error, Warning) inside modal */
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

    st.write("Enter the details of new subject")
    sub_id = st.text_input("Subject Code", placeholder="CS101")
    sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="A")

    if st.button("Create Subject Now", type='primary', width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast("Subject Created Succesfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill all the fields")
