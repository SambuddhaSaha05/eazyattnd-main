import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            border-left: 6px solid #4338CA;
            padding: 22px 24px;
            border-radius: 16px;
            box-shadow: 0 8px 20px -4px rgba(15, 23, 42, 0.07);
            margin-bottom: 18px;
        ">
            <h3 style="
                margin: 0;
                color: #0F172A !important;
                font-size: 1.35rem;
                font-weight: 700;
                letter-spacing: -0.01em;
            ">{name}</h3>
            <p style="
                color: #475569 !important;
                margin: 10px 0 14px 0;
                font-size: 0.95rem;
                font-weight: 500;
            ">
                Code:
                <span style="
                    background: #EEF2FF;
                    color: #4338CA !important;
                    border: 1px solid #C7D2FE;
                    padding: 3px 10px;
                    border-radius: 6px;
                    font-weight: 600;
                    font-size: 0.88rem;
                    margin: 0 4px;
                ">{code}</span>
                &nbsp;|&nbsp;
                Section: <strong style="color: #0F172A !important;">{section}</strong>
            </p>
    """

    if stats:
        html += """
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        """
        for icon, label, value in stats:
            html += f"""
                <div style="
                    background: #F8FAFC;
                    border: 1px solid #E2E8F0;
                    color: #0F172A !important;
                    padding: 6px 14px;
                    border-radius: 10px;
                    font-size: 0.9rem;
                    font-weight: 500;
                ">{icon} <strong style="color: #0F172A !important;">{value}</strong> <span style="color: #475569 !important;">{label}</span></div>
            """
        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
