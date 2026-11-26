import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from PIL import Image
import time


@st.dialog("Capture or upload photos")
def add_photos_dialog():
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
        div[role="dialog"] label,
        div[role="dialog"] small {
            color: #0F172A !important;
        }

        /* File uploader dropzone */
        div[role="dialog"] section[data-testid="stFileUploaderDropzone"] {
            background-color: #F8FAFC !important;
            border: 1.5px dashed #94A3B8 !important;
            border-radius: 14px !important;
            color: #0F172A !important;
        }

        div[role="dialog"] section[data-testid="stFileUploaderDropzone"] button {
            background-color: #EEF2FF !important;
            color: #4338CA !important;
            border: 1px solid #C7D2FE !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
        }

        /* Primary buttons (Active tab, Done) - Deep Indigo Gradient */
        div[role="dialog"] button[data-testid="stBaseButton-primary"],
        div[role="dialog"] button[kind="primary"] {
            background: linear-gradient(135deg, #4338CA 0%, #2563EB 100%) !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.22) !important;
        }

        /* Tertiary buttons (Inactive tab) - Dark Slate */
        div[role="dialog"] button[data-testid="stBaseButton-tertiary"],
        div[role="dialog"] button[kind="tertiary"] {
            background-color: #1E293B !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
        }

        /* Keep white text strictly inside primary/tertiary buttons */
        div[role="dialog"] button[data-testid="stBaseButton-primary"] p,
        div[role="dialog"] button[data-testid="stBaseButton-primary"] span,
        div[role="dialog"] button[kind="primary"] p,
        div[role="dialog"] button[kind="primary"] span,
        div[role="dialog"] button[data-testid="stBaseButton-tertiary"] p,
        div[role="dialog"] button[data-testid="stBaseButton-tertiary"] span,
        div[role="dialog"] button[kind="tertiary"] p,
        div[role="dialog"] button[kind="tertiary"] span {
            color: #FFFFFF !important;
        }

        div[role="dialog"] hr {
            border-color: #E2E8F0 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    st.write('Add classroom photos to scan for attendance')

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'tertiary'
        if st.button('Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'

    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'tertiary'
        if st.button('Upload photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Take Snapshot', key='dialog_cam')
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast('Photo Captured')
            st.rerun()

    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader('choose image files', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key='dialog_upload')

        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))

            st.toast('Photo Uploaded Successfully')
            st.rerun()

    st.divider()
    if st.button('Done', type='primary', width='stretch'):
        st.rerun()
