import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    stats_html = ""
    if stats:
        chips = "".join(
            f'<div style="background:#F8FAFC; border:1px solid #E2E8F0; color:#0F172A; padding:6px 14px; border-radius:10px; font-size:0.9rem; font-weight:500;">'
            f'{icon} <strong style="color:#0F172A;">{value}</strong> <span style="color:#475569;">{label}</span>'
            f'</div>'
            for icon, label, value in stats
        )
        stats_html = f'<div style="display:flex; gap:10px; flex-wrap:wrap;">{chips}</div>'

    html = (
        f'<div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:6px solid #4338CA; '
        f'padding:22px 24px; border-radius:16px; box-shadow:0 8px 20px -4px rgba(15, 23, 42, 0.07); margin-bottom:18px;">'
        f'<h3 style="margin:0; color:#0F172A; font-size:1.35rem; font-weight:700; letter-spacing:-0.01em;">{name}</h3>'
        f'<p style="color:#475569; margin:10px 0 14px 0; font-size:0.95rem; font-weight:500;">'
        f'Code: <span style="background:#EEF2FF; color:#4338CA; border:1px solid #C7D2FE; padding:3px 10px; '
        f'border-radius:6px; font-weight:600; font-size:0.88rem; margin:0 4px;">{code}</span>'
        f' &nbsp;|&nbsp; Section: <strong style="color:#0F172A;">{section}</strong>'
        f'</p>'
        f'{stats_html}'
        f'</div>'
    )

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
