import streamlit as st

def apply_custom_css():
    st.markdown(
        """
        <style>
        /* Make buttons red and rounded */
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 10px;
            padding: 0.5em 1em;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #FF1C1C;
            color: #fff;
        }

        /* Center titles */
        .stApp h1 {
            text-align: center;
        }

        /* Style the top prediction box */
        .stSuccess {
            font-size: 18px;
            font-weight: bold;
            border-radius: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
