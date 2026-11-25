
import streamlit as st
from textwrap import dedent


def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        dedent(f"""
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
            margin-top: 10px;
        ">
            <img
                src="{logo_url}"
                style="height: 100px; width: auto; object-fit: contain;"
            />

            <h1 style="
                text-align: center;
                color: #E0E3FF;
                margin-top: 10px;
            ">
                EAZY<br>ATTND
            </h1>
        </div>
        """),
        unsafe_allow_html=True
    )


def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        dedent(f"""
        <div style="
            display: flex;
            align-items: center;
            justify-content: flex-start;
            gap: 10px;
            flex-wrap: wrap;
        ">
            <img
                src="{logo_url}"
                style="
                    height: 85px;
                    width: auto;
                    object-fit: contain;
                "
            />

            <div style="
                font-family: 'Climate Crisis', sans-serif;
                font-size: 2rem;
                line-height: 0.95;
                text-align: left;
                color: #000000;
            ">
                EAZY<br>ATTND
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )


