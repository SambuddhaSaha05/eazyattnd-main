import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
import time

from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card


def style_student_theme():
    st.markdown("""
    <style>
        /* Force clean light background so dark text always has high contrast */
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"] {
            background: linear-gradient(180deg, #F8FAFC 0%, #EEF2FF 100%) !important;
            color: #0F172A !important;
        }

        /* All headings (including st.subheader for Welcome, Name) */
        h1, h2, h3, h4, h5, h6,
        div[data-testid="stHeading"] h1,
        div[data-testid="stHeading"] h2,
        div[data-testid="stHeading"] h3,
        div[data-testid="stHeading"] h4 {
            color: #0F172A !important;
            font-weight: 700 !important;
        }

        /* All general text, markdown, captions, and spinner text */
        p, span, label, div[data-testid="stText"],
        div[data-testid="stMarkdownContainer"] p,
        div[data-testid="stMarkdownContainer"] span,
        div[data-testid="stMarkdownContainer"] strong,
        div[data-testid="stSpinner"] p,
        div[data-testid="stSpinner"] div {
            color: #1E293B !important;
        }

        /* Widget labels (Text input, Camera input, Audio input) */
        div[data-testid="stWidgetLabel"] p,
        div[data-testid="stWidgetLabel"] label,
        div[data-testid="stCameraInput"] label,
        div[data-testid="stAudioInput"] label {
            color: #0F172A !important;
            font-weight: 600 !important;
        }

        /* Bordered containers (Registration form & cards) */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #FFFFFF !important;
            border: 1.5px solid #CBD5E1 !important;
            border-radius: 16px !important;
            padding: 1.25rem !important;
            box-shadow: 0 8px 20px -4px rgba(15, 23, 42, 0.08) !important;
        }

        /* Text inputs */
        input, textarea {
            background-color: #FFFFFF !important;
            color: #0F172A !important;
            -webkit-text-fill-color: #0F172A !important;
            border: 1.5px solid #94A3B8 !important;
            border-radius: 10px !important;
        }

        input:focus, textarea:focus {
            border-color: #4338CA !important;
            box-shadow: 0 0 0 3px rgba(67, 56, 202, 0.18) !important;
        }

        input::placeholder, textarea::placeholder {
            color: #64748B !important;
            opacity: 1 !important;
            -webkit-text-fill-color: #64748B !important;
        }

        /* Primary buttons (Enroll in Subject, Create Account) - Deep Indigo */
        button[data-testid="stBaseButton-primary"],
        button[kind="primary"] {
            background: linear-gradient(135deg, #4338CA 0%, #2563EB 100%) !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
        }

        /* Secondary buttons (Logout, Go back to Home) - Crisp Rose */
        button[data-testid="stBaseButton-secondary"],
        button[kind="secondary"] {
            background-color: #E11D48 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 10px rgba(225, 29, 72, 0.22) !important;
        }

        /* Tertiary buttons (Unenroll) - Dark Slate */
        button[data-testid="stBaseButton-tertiary"],
        button[kind="tertiary"] {
            background-color: #1E293B !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
        }

        /* Keep white text strictly inside action buttons */
        button[data-testid="stBaseButton-primary"] p,
        button[data-testid="stBaseButton-primary"] span,
        button[kind="primary"] p,
        button[kind="primary"] span,
        button[data-testid="stBaseButton-secondary"] p,
        button[data-testid="stBaseButton-secondary"] span,
        button[kind="secondary"] p,
        button[kind="secondary"] span,
        button[data-testid="stBaseButton-tertiary"] p,
        button[data-testid="stBaseButton-tertiary"] span,
        button[kind="tertiary"] p,
        button[kind="tertiary"] span {
            color: #FFFFFF !important;
        }

        button:hover {
            opacity: 0.92 !important;
            transform: translateY(-1px) !important;
            transition: all 0.2s ease-in-out !important;
        }

        /* Alerts (st.warning, st.info, st.error) */
        div[data-testid="stAlert"] {
            background-color: #FFFFFF !important;
            border: 1.5px solid #CBD5E1 !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 10px rgba(15, 23, 42, 0.06) !important;
        }

        div[data-testid="stAlert"] p,
        div[data-testid="stAlert"] span {
            color: #0F172A !important;
            font-weight: 500 !important;
        }

        /* Divider */
        hr {
            border-color: #CBD5E1 !important;
        }
    </style>
    """, unsafe_allow_html=True)


def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"""Welcome, {student_data['name']} """)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    st.space()

    c1, c2 = st.columns(2)
    with c1:
        st.header('Your Enrolled Subjects')
    with c2:
        if st.button('Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}

        stats_map[sid]['total'] += 1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']

        stats = stats_map.get(sid, {"total": 0, "attended": 0})

        def unenroll_button(subject_id=sid, subject_name=sub['name']):
            if st.button(
                "Unenroll from this course",
                key=f"unenroll_{subject_id}",
                type='tertiary',
                width='stretch',
                icon=':material/delete_forever:'
            ):
                unenroll_student_to_subject(student_id, subject_id)
                st.toast(f'Unenrolled from {subject_name} successfully!')
                st.rerun()

        with cols[i % 2]:
            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=[
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
                footer_callback=unenroll_button
            )
    footer_dashboard()


def student_screen():

    style_background_dashboard()
    style_base_layout()
    style_student_theme()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header('Login using FaceID', text_alignment='center')
    st.space()
    st.space()

    show_registration = False
    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner('AI is scanning..'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('Face not found!')
            elif num_faces > 1:
                st.warning('Multiple faces found')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f'Welcome Back {student["name"]}')
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('Face not recognized! You might be a new student!')
                    show_registration = True
    if show_registration:
        with st.container(border=True):
            st.header('Register new Profile')
            new_name = st.text_input("Enter your name", placeholder='E.g. Hamza Rizvi')

            st.subheader('Optional : Voice Enrollment')
            st.info("Enroll your for voice only attendance")

            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like I am present, My name is Akash.')
            except Exception:
                st.error('Audio Data failed!')

            if st.button('Create Account', type='primary'):
                if new_name:
                    with st.spinner('Creating profile..'):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Hi {new_name}!')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error('Couldnt capture your facial features for registration')

                else:
                    st.warning('Please enter your name!')

    footer_dashboard()
