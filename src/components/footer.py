
import streamlit as st

def footer_home():
    logo_url = "https://i.postimg.cc/VkGvBt8M/Gemini-Generated-Image-r8qelvr8qelvr8qe.png"

    st.markdown(f"""
          <div style="margin-top:5rem; display:flex; justify-content:center; align-items:center; gap:10px;">
            <p style="font-weight:bold; color:black;">Created<br/>by</p>
            <img src="{logo_url}" style="height:50px;" />
        </div>
    """, unsafe_allow_html=True)
    
