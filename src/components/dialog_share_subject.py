import streamlit as st

import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
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

        /* Headings, text, and QR caption inside modal */
        div[role="dialog"] h1,
        div[role="dialog"] h2,
        div[role="dialog"] h3,
        div[role="dialog"] p,
        div[role="dialog"] span,
        div[role="dialog"] div[data-testid="stCaptionContainer"] p {
            color: #0F172A !important;
        }

        /* High-contrast code boxes for Copy Link & Subject Code */
        div[role="dialog"] pre,
        div[role="dialog"] code,
        div[role="dialog"] div[data-testid="stCode"] {
            background-color: #F1F5F9 !important;
            color: #0F172A !important;
            border: 1px solid #CBD5E1 !important;
            border-radius: 10px !important;
        }

        /* Info box inside modal */
        div[role="dialog"] div[data-testid="stAlert"] {
            background-color: #EEF2FF !important;
            border: 1px solid #C7D2FE !important;
            border-radius: 10px !important;
        }

        div[role="dialog"] div[data-testid="stAlert"] p,
        div[role="dialog"] div[data-testid="stAlert"] span {
            color: #1E293B !important;
            font-weight: 500 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    app_domain = "https://eazyattnd-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join")

    qr = segno.make(join_url)

    out = io.BytesIO()

    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('### Copy Link')
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info('Copy this link to share on Whatsapp or Email')

    with col2:
        st.markdown('### Scan to Join')
        st.image(out.getvalue(), caption='QRCODE for class joining')
