import streamlit as st


LOGO_URL = "https://i.ibb.co/YTYGn5qV/logo.png"


def header_home():
    st.markdown(
        f"""
        <div style="
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            padding:20px 0;
        ">
            <img src="{LOGO_URL}" style="
                height:110px;
                width:auto;
                object-fit:contain;
            "/>

            <h1 style="
                color:#111827;
                font-size:42px;
                font-weight:900;
                text-align:center;
                margin:10px 0 0 0;
            ">
                EAZY ATTND
            </h1>

            <p style="
                color:#64748B;
                font-size:16px;
                margin-top:5px;
            ">
                Smart Attendance Management System
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def header_dashboard(name, role="Dashboard"):
    st.markdown(
        f"""
        <div style="
            display:flex;
            align-items:center;
            justify-content:space-between;
            flex-wrap:wrap;
            background:#FFFFFF;
            padding:18px 24px;
            border-radius:18px;
            border:1px solid #DCE6F1;
            margin-bottom:25px;
        ">

            <div style="
                display:flex;
                align-items:center;
                gap:15px;
            ">
                <img src="{LOGO_URL}" style="
                    height:65px;
                    width:auto;
                    object-fit:contain;
                "/>

                <div>
                    <h2 style="
                        margin:0;
                        font-size:26px;
                        color:#111827;
                        font-weight:900;
                    ">
                        EAZY ATTND
                    </h2>

                    <p style="
                        margin:3px 0 0 0;
                        color:#64748B;
                        font-size:13px;
                    ">
                        Attendance Management System
                    </p>
                </div>
            </div>

            <div style="
                text-align:right;
                padding:10px;
            ">
                <p style="
                    margin:0;
                    color:#64748B;
                    font-size:14px;
                ">
                    {role}
                </p>

                <h3 style="
                    margin:5px 0 0 0;
                    color:#111827;
                    font-size:24px;
                    font-weight:800;
                ">
                    Welcome, {name}
                </h3>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
