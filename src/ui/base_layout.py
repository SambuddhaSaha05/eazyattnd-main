
import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

            .stApp {
                background: #5865F2 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 1.2rem !important;
                border-radius: 2rem !important;
            }

        </style>
    """, unsafe_allow_html=True)



def style_background_dashboard():

    st.markdown("""
        <style>

            .stApp {
                background-color: #DFF6FF !important;
            }

        </style>
    """, unsafe_allow_html=True)



def style_base_layout():

    st.markdown("""
        <style>

            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');

            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');


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


            /* MAIN HEADING */

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: clamp(1.7rem, 3vw, 2.8rem) !important;
                font-weight: 800 !important;
                margin-bottom: 0.5rem !important;
                text-align: center;
                color: black !important;
            }


            /* SECTION HEADINGS */

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: clamp(1.35rem, 2.2vw, 2rem) !important;
                line-height: 1.2 !important;
                margin-bottom: 0.5rem !important;
                color: black !important;

                /* Prevent heading overlap */

                white-space: normal !important;
                overflow-wrap: break-word !important;
                word-break: normal !important;
            }


            /* BODY FONT */

            h3,
            h4,
            h5,
            p,
            label {
                font-family: 'Outfit', sans-serif !important;
            }


            /* PRIMARY BUTTON */

            button {
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }


            /* SECONDARY BUTTON */

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }


            /* TERTIARY BUTTON */

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }


            /* BUTTON HOVER */

            button:hover {
                transform: translateY(-1px);
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

                button {
                    padding: 8px 12px !important;
                }

            }

        </style>
    """, unsafe_allow_html=True)

# import streamlit as st



# def style_background_home():
#     st.markdown("""
#         <style>
#             .stApp{
#             background: #5865F2 !important;
#             }
                
#             .stApp div[data-testid="stColumn"]{
#                 background-color: #E0E3FF !important;
#                 padding: 1.2rem !important;
#                 border-radius: 2rem !important;
#             }
#         </style>
#     """, unsafe_allow_html=True)



# # def style_base_dashboard():
# #     st.markdown("""
# #         <style>
# #         .stApp {
# #             background-color: #E0E3FF !important;
# #         }
# #         </style>
# #     """, unsafe_allow_html=True)

# def style_background_dashboard():
#     st.markdown("""
#         <style>
#         .stApp {
#             background-color: #DFF6FF !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)


# def style_base_layout():
#     st.markdown("""
#         <style>
#             @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
#             @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
#             /* Hide Top Bar of Streamlit */
#             MainMenu, footer, header {
#                 visibility: hidden;
#             }

#             .block-container {
#             padding-top: 0rem !important;
#             padding-bottom: 0rem !important;
#             }
            
#             h1{
#                 font-family: 'Climate Crisis', sans-serif !important;
#                 font-size: 2.8rem !important;
#                 font-weight: 800 !important;
#                 margin-bottom: 0.1rem !important;
#                 text-align: center;
#                 color: black !important;
            
#             }
                
#             h2{
#                 font-family: 'Climate Crisis', sans-serif !important;
#                 font-size: 2.2rem !important;
#                 line-height: 0.9 !important;
#                 margin-bottom: 0rem !important;
                
#                 color: black !important;
#                 white-space: nowrap !important; 

              
#             }
                
#             h3, h4, p{
#                 font-family: 'Outfit', sans-serif !important;

#             }
                
#             button{
#                 border-radius: 1.5rem !important;
#                 background-color: #5865F2 !important;
#                 color: white !important;
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;              
#             }   
#             button[kind="secondary"]{
#                 border-radius: 1.5rem !important;
#                 background-color: #EB459E !important;
#                 color: white !important;
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;                
#             }     
                
#             button[kind="tertiary"]{
#                 border-radius: 1.5rem !important;
#                 background-color: black !important;
#                 color: white !important;
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;                  
#             }    
                
#             button:hover{
#                 transform: scale(1.05)
#             }
#             html, body, [data-testid="stAppViewContainer"] {
#             height: 100vh;
#             overflow: hidden;
#         }
                




           
#             </style>
#         """, unsafe_allow_html=True)
