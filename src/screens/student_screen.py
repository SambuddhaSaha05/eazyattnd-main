
import streamlit as st
from html import escape

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from PIL import Image
import numpy as np

from src.pipelines.face_pipeline import (
    predict_attendance,
    get_face_embeddings,
    train_classifier
)

from src.pipelines.voice_pipeline import get_voice_embedding

from src.database.db import (
    get_all_students,
    create_student,
    get_student_subjects,
    get_student_attendance,
    unenroll_student_to_subject
)

import time

from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card


# ==========================================================
# STUDENT DASHBOARD
# ==========================================================

def student_dashboard():

    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    student_name = escape(str(student_data.get('name', 'Student')))

    # ------------------------------------------------------
    # DASHBOARD STYLING
    # ------------------------------------------------------

    st.markdown("""
        <style>
            .student-welcome {
                color: #172554 !important;
                font-size: clamp(20px, 2vw, 30px) !important;
                font-weight: 800 !important;
                text-align: right !important;
                line-height: 1.4 !important;
                overflow-wrap: anywhere !important;
                margin: 0 0 12px 0 !important;
            }

            .student-section-heading {
                color: #172554 !important;
                font-weight: 800 !important;
            }

            .student-dashboard-caption {
                color: #475569 !important;
                font-size: 14px !important;
            }

            div[data-testid="stButton"] button {
                min-height: 44px;
                border-radius: 14px !important;
                font-weight: 600 !important;
            }

            div[data-testid="stVerticalBlock"] {
                gap: 0.8rem;
            }

            @media (max-width: 768px) {
                .student-welcome {
                    text-align: left !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    # ------------------------------------------------------
    # TOP HEADER
    # ------------------------------------------------------

    header_col, welcome_col = st.columns(
        [1.2, 1],
        vertical_alignment="center",
        gap="medium"
    )

    with header_col:
        header_dashboard()

    with welcome_col:

        st.markdown(
            f"""
            <div class="student-welcome">
                Welcome, {student_name}
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Logout",
            type="secondary",
            key="student_logout_button",
            width="stretch"
        ):
            st.session_state['is_logged_in'] = False
            st.session_state.pop('student_data', None)
            st.rerun()

    st.divider()

    # ------------------------------------------------------
    # ENROLLED SUBJECTS HEADING
    # ------------------------------------------------------

    st.header("Your Enrolled Subjects")

    st.caption("View your subjects and attendance statistics.")

    # Place enrollment button below the heading to avoid overlap
    if st.button(
        "➕ Enroll in Subject",
        type="primary",
        key="student_enroll_subject_button",
        width="stretch"
    ):
        enroll_dialog()

    st.divider()

    # ------------------------------------------------------
    # FETCH SUBJECTS AND ATTENDANCE
    # ------------------------------------------------------

    with st.spinner("Loading your enrolled subjects..."):

        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    # ------------------------------------------------------
    # ATTENDANCE STATISTICS
    # ------------------------------------------------------

    stats_map = {}

    for log in logs:

        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {
                "total": 0,
                "attended": 0
            }

        stats_map[sid]['total'] += 1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    # ------------------------------------------------------
    # DISPLAY SUBJECTS
    # ------------------------------------------------------

    if not subjects:

        st.info(
            "You are not enrolled in any subjects yet. "
            "Click 'Enroll in Subject' above to get started."
        )

    else:

        cols = st.columns(2, gap="medium")

        for i, sub_node in enumerate(subjects):

            sub = sub_node['subjects']
            sid = sub['subject_id']

            stats = stats_map.get(
                sid,
                {
                    "total": 0,
                    "attended": 0
                }
            )

            # --------------------------------------------------
            # UNENROLL BUTTON
            # --------------------------------------------------

            def unenroll_button(subject_id=sid, subject_name=sub['name']):

                if st.button(
                    "Unenroll from this course",
                    key=f"unenroll_{subject_id}",
                    type="tertiary",
                    width="stretch",
                    icon=":material/delete_forever:"
                ):

                    unenroll_student_to_subject(student_id, subject_id)

                    st.toast(
                        f"Unenrolled from {subject_name} successfully!"
                    )

                    st.rerun()

            # --------------------------------------------------
            # SUBJECT CARD
            # --------------------------------------------------

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

    # ------------------------------------------------------
    # FOOTER
    # ------------------------------------------------------

    footer_dashboard()


# ==========================================================
# STUDENT LOGIN / REGISTRATION SCREEN
# ==========================================================

def student_screen():

    style_background_dashboard()
    style_base_layout()

    # ------------------------------------------------------
    # ALREADY LOGGED IN
    # ------------------------------------------------------

    if "student_data" in st.session_state:

        student_dashboard()
        return

    # ------------------------------------------------------
    # LOGIN PAGE HEADER
    # ------------------------------------------------------

    header_col, back_col = st.columns(
        [1.2, 1],
        vertical_alignment="center",
        gap="medium"
    )

    with header_col:
        header_dashboard()

    with back_col:

        if st.button(
            "Go back to Home",
            type="secondary",
            key="student_back_home_button",
            width="stretch"
        ):
            st.session_state['login_type'] = None
            st.rerun()

    # ------------------------------------------------------
    # FACE ID LOGIN
    # ------------------------------------------------------

    st.header(
        "Login using FaceID",
        text_alignment="center"
    )

    st.caption(
        "Position your face clearly in front of the camera."
    )

    photo_source = st.camera_input(
        "Position your face in the center"
    )

    show_registration = False

    # ------------------------------------------------------
    # FACE RECOGNITION
    # ------------------------------------------------------

    if photo_source:

        img = np.array(Image.open(photo_source))

        with st.spinner("AI is scanning..."):

            detected, all_ids, num_faces = predict_attendance(img)

        if num_faces == 0:

            st.warning("Face not found!")

        elif num_faces > 1:

            st.warning("Multiple faces found. Please try again with only one face.")

        else:

            if detected:

                student_id = list(detected.keys())[0]

                all_students = get_all_students()

                student = next(
                    (
                        s for s in all_students
                        if s['student_id'] == student_id
                    ),
                    None
                )

                if student:

                    st.session_state.is_logged_in = True
                    st.session_state.user_role = 'student'
                    st.session_state.student_data = student

                    st.toast(
                        f"Welcome back, {student['name']}!",
                        icon="👋"
                    )

                    time.sleep(1)
                    st.rerun()

            else:

                st.info(
                    "Face not recognized. You might be a new student!"
                )

                show_registration = True

    # ------------------------------------------------------
    # NEW STUDENT REGISTRATION
    # ------------------------------------------------------

    if show_registration:

        with st.container(border=True):

            st.header("Register New Profile")

            new_name = st.text_input(
                "Enter your name",
                placeholder="E.g. Hamza Rizvi"
            )

            st.divider()

            # ----------------------------------------------
            # VOICE ENROLLMENT
            # ----------------------------------------------

            st.subheader("Optional: Voice Enrollment")

            st.info(
                "You can enroll your voice to use voice-based attendance."
            )

            audio_data = None

            try:

                audio_data = st.audio_input(
                    "Record a short phrase, such as "
                    "'I am present' or 'My name is ...'"
                )

            except Exception:

                st.error("Audio data could not be captured.")

            # ----------------------------------------------
            # CREATE ACCOUNT
            # ----------------------------------------------

            if st.button(
                "Create Account",
                type="primary",
                key="student_create_account_button"
            ):

                if not new_name.strip():

                    st.warning("Please enter your name!")

                else:

                    with st.spinner("Creating your profile..."):

                        img = np.array(Image.open(photo_source))

                        encodings = get_face_embeddings(img)

                        if encodings:

                            face_emb = encodings[0].tolist()

                            voice_emb = None

                            if audio_data:

                                voice_emb = get_voice_embedding(
                                    audio_data.read()
                                )

                            response_data = create_student(
                                new_name.strip(),
                                face_embedding=face_emb,
                                voice_embedding=voice_emb
                            )

                            if response_data:

                                train_classifier()

                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]

                                st.toast(
                                    f"Profile created! Hi {new_name}!",
                                    icon="👋"
                                )

                                time.sleep(1)
                                st.rerun()

                        else:

                            st.error(
                                "Could not capture your facial features. "
                                "Please try again with better lighting."
                            )

    # ------------------------------------------------------
    # FOOTER
    # ------------------------------------------------------

    footer_dashboard()
