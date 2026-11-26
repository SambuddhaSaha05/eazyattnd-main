import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 1.5rem;
            margin-bottom: 2rem;
            gap: 12px;
        ">
            <img src="{logo_url}" style="
                height: 96px;
                filter: drop-shadow(0 6px 14px rgba(67, 56, 202, 0.18));
            " />
            <h1 style="
                text-align: center;
                margin: 0;
                line-height: 1.05;
                background: linear-gradient(135deg, #312E81 0%, #4338CA 55%, #2563EB 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                color: #4338CA !important;
                letter-spacing: 0.02em;
            ">EAZY<br/>ATTEND</h1>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="
            display: flex;
            align-items: center;
            justify-content: flex-start;
            gap: 14px;
        ">
            <img src="{logo_url}" style="
                height: 76px;
                filter: drop-shadow(0 4px 10px rgba(67, 56, 202, 0.16));
            " />
            <h2 style="
                text-align: left;
                margin: 0;
                line-height: 1.08;
                font-weight: 800;
                background: linear-gradient(135deg, #312E81 0%, #4338CA 55%, #2563EB 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                color: #4338CA !important;
                letter-spacing: -0.01em;
            ">EAZY<br/>ATTEND</h2>
        </div>
    """, unsafe_allow_html=True)
