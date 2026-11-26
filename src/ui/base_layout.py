import streamlit as st


def style_background_home():

    st.markdown("""
        <style>
            /* Soft, modern pearl-indigo atmospheric gradient so header, cards, and footer all pop */
            .stApp {
                background: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 50%, #E0E7FF 100%) !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: rgba(255, 255, 255, 0.95) !important;
                border: 1px solid #E2E8F0 !important;
                padding: 1.5rem !important;
                border-radius: 1.5rem !important;
                box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.08) !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>
            /* Clean, calm slate-mist background for high readability across dashboards */
            .stApp {
                background: linear-gradient(180deg, #F8FAFC 0%, #F1F5F9 100%) !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

            /* Hide Streamlit top menu and footer */
            #MainMenu,
            footer,
            header {
                visibility: hidden;
            }

            /* MAIN PAGE CONTAINER */
            .block-container {
                max-width: 1200px !important;
                padding-top: 1.5rem !important;
                padding-bottom: 3rem !important;
                padding-left: 2rem !important;
                padding-right: 2rem !important;
            }

            /* MAIN BRAND HEADING */
            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: clamp(1.7rem, 3vw, 2.8rem) !important;
                font-weight: 800 !important;
                margin-bottom: 0.5rem !important;
                text-align: center;
                color: #0F172A !important;
                letter-spacing: 0.01em !important;
            }

            /* SECTION & NAME HEADINGS - Crisp Outfit font so names never clip or blur */
            h2 {
                font-family: 'Outfit', sans-serif !important;
                font-size: clamp(1.35rem, 2.2vw, 1.9rem) !important;
                font-weight: 700 !important;
                line-height: 1.25 !important;
                margin-bottom: 0.5rem !important;
                color: #0F172A !important;
                white-space: normal !important;
                overflow-wrap: break-word !important;
                word-break: normal !important;
            }

            /* BODY FONT & BASE TEXT CONTRAST */
            h3,
            h4,
            h5,
            p,
            span,
            label,
            div[data-testid="stMarkdownContainer"] p {
                font-family: 'Outfit', sans-serif !important;
                color: #1E293B;
            }

            /* PRIMARY BUTTON (Scoped so internal Streamlit UI icons aren't broken) */
            button[data-testid="stBaseButton-primary"],
            button[kind="primary"] {
                border-radius: 0.85rem !important;
                background: linear-gradient(135deg, #4338CA 0%, #2563EB 100%) !important;
                color: #FFFFFF !important;
                padding: 10px 20px !important;
                border: none !important;
                font-weight: 600 !important;
                box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
                transition: all 0.2s ease-in-out !important;
            }

            /* SECONDARY BUTTON */
            button[data-testid="stBaseButton-secondary"],
            button[kind="secondary"] {
                border-radius: 0.85rem !important;
                background-color: #E11D48 !important;
                color: #FFFFFF !important;
                padding: 10px 20px !important;
                border: none !important;
                font-weight: 600 !important;
                box-shadow: 0 4px 10px rgba(225, 29, 72, 0.18) !important;
                transition: all 0.2s ease-in-out !important;
            }

            /* TERTIARY BUTTON */
            button[data-testid="stBaseButton-tertiary"],
            button[kind="tertiary"] {
                border-radius: 0.85rem !important;
                background-color: #1E293B !important;
                color: #FFFFFF !important;
                padding: 10px 20px !important;
                border: none !important;
                font-weight: 600 !important;
                transition: all 0.2s ease-in-out !important;
            }

            /* BUTTON TEXT COLOR */
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

            /* BUTTON HOVER */
            button[data-testid="stBaseButton-primary"]:hover,
            button[data-testid="stBaseButton-secondary"]:hover,
            button[data-testid="stBaseButton-tertiary"]:hover {
                transform: translateY(-1px) !important;
                opacity: 0.94 !important;
            }

            /* PAGE SCROLLING */
            html,
            body,
            [data-testid="stAppViewContainer"],
            [data-testid="stMain"] {
                min-height: 100% !important;
                height: auto !important;
                overflow-y: auto !important;
                overflow-x: hidden !important;
            }

            /* PREVENT COLUMN CONTENT FROM OVERFLOWING */
            [data-testid="stHorizontalBlock"] {
                align-items: center;
                gap: 1rem;
            }

            /* RESPONSIVE LAYOUT FOR TABLETS AND MOBILE */
            @media (max-width: 768px) {
                .block-container {
                    padding-top: 1rem !important;
                    padding-bottom: 2rem !important;
                    padding-left: 1rem !important;
                    padding-right: 1rem !important;
                }

                h1 {
                    font-size: clamp(1.5rem, 6vw, 2rem) !important;
                }

                h2 {
                    font-size: clamp(1.2rem, 5vw, 1.6rem) !important;
                    line-height: 1.25 !important;
                }
            }

            /* SMALL MOBILE SCREENS */
            @media (max-width: 480px) {
                .block-container {
                    padding-left: 0.8rem !important;
                    padding-right: 0.8rem !important;
                }

                button[data-testid="stBaseButton-primary"],
                button[data-testid="stBaseButton-secondary"],
                button[data-testid="stBaseButton-tertiary"] {
                    padding: 8px 12px !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)
