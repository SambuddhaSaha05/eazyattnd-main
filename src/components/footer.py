import streamlit as st


def footer_home():
    logo_url = "https://lh3.googleusercontent.com/d/17Ws8-1jPUz0XD3kvvrwKGJjPgYI-u0t7"

    st.markdown(f"""
        <div style="
            margin-top: 2.5rem;
            padding-top: 1.25rem;
            border-top: 1px solid #CBD5E1;
            display: flex;
            gap: 8px;
            justify-content: center;
            align-items: center;
        ">
            <p style="
                margin: 0;
                font-weight: 600;
                font-size: 0.92rem;
                color: #334155 !important;
                letter-spacing: 0.01em;
            ">Created with ❤️ by</p>
            <img src="{logo_url}" style="max-height: 24px; border-radius: 4px;" />
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://lh3.googleusercontent.com/d/17Ws8-1jPUz0XD3kvvrwKGJjPgYI-u0t7"

    st.markdown(f"""
        <div style="
            margin-top: 2.5rem;
            padding-top: 1.25rem;
            border-top: 1px solid #CBD5E1;
            display: flex;
            gap: 8px;
            justify-content: center;
            align-items: center;
        ">
            <p style="
                margin: 0;
                font-weight: 600;
                font-size: 0.92rem;
                color: #334155 !important;
                letter-spacing: 0.01em;
            ">Created with ❤️ by</p>
            <img src="{logo_url}" style="max-height: 24px; border-radius: 4px;" />
        </div>
    """, unsafe_allow_html=True)
