import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def style_home_theme():
    st.markdown("""
    <style>
        /* Force clean light background so header, cards, and footer all have high contrast */
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"] {
            background: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 50%, #E0E7FF 100%) !important;
            color: #0F172A !important;
        }

        /* Elevated crisp white portal cards for the two columns */
        div[data-testid="stColumn"] {
            background-color: #FFFFFF !important;
            border: 1.5px solid #CBD5E1 !important;
            border-radius: 18px !important;
            padding: 2rem 1.75rem !important;
            box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.08),
                        0 8px 10px -6px rgba(15, 23, 42, 0.04) !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease !important;
        }

        div[data-testid="stColumn"]:hover {
            transform: translateY(-3px) !important;
            border-color: #4338CA !important;
            box-shadow: 0 20px 25px -5px rgba(15, 23, 42, 0.12),
                        0 8px 10px -6px rgba(15, 23, 42, 0.06) !important;
        }

        /* All headings (Brand title, I'm Student, I'm Teacher) */
        h1, h2, h3, h4, h5, h6,
        div[data-testid="stHeading"] h1,
        div[data-testid="stHeading"] h2,
        div[data-testid="stHeading"] h3,
        div[data-testid="stHeading"] h4 {
            color: #0F172A !important;
            font-weight: 700 !important;
        }

        /* All general text, markdown, and footer text */
        p, span, label,
        div[data-testid="stMarkdownContainer"] p,
        div[data-testid="stMarkdownContainer"] span,
        div[data-testid="stMarkdownContainer"] strong {
            color: #1E293B !important;
        }

        /* Primary Portal buttons - Deep Indigo Gradient */
        button[data-testid="stBaseButton-primary"],
        button[kind="primary"] {
            background: linear-gradient(135deg, #4338CA 0%, #2563EB 100%) !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.65rem 1.4rem !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
        }

        button[data-testid="stBaseButton-primary"] p,
        button[data-testid="stBaseButton-primary"] span,
        button[kind="primary"] p,
        button[kind="primary"] span {
            color: #FFFFFF !important;
        }

        button[data-testid="stBaseButton-primary"]:hover,
        button[kind="primary"]:hover {
            background: linear-gradient(135deg, #3730A3 0%, #1D4ED8 100%) !important;
            transform: translateY(-1px) !important;
            transition: all 0.2s ease-in-out !important;
        }

        /* Divider */
        hr {
            border-color: #CBD5E1 !important;
        }
    </style>
    """, unsafe_allow_html=True)


def home_screen():

    header_home()
    style_background_home()
    style_base_layout()
    style_home_theme()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()
