import streamlit as st

def load_css(theme):
    if theme == 'dark':
        background_color = "#0E1117"
        text_color = "#FFFFFF"
        card_bg_color = "#262730"
        secondary_bg = "#1E1E1E"
    else:
        background_color = "#FFFFFF"
        text_color = "#000000"
        card_bg_color = "#F0F2F6"
        secondary_bg = "#EAEAEA"

    st.markdown(f"""
    <style>
    .main {{
        background-color: {background_color};
        color: {text_color};
    }}
    
    .main-header {{
        background-color: {card_bg_color};
        color: {text_color};
        text-align: center;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    
    .school-name {{
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 5px;
        color: {text_color};
    }}
    
    .school-address {{
        font-size: 1.2em;
        color: {'#666666' if theme == 'light' else '#CCCCCC'};
    }}
    
    .question-box {{
        background-color: {card_bg_color};
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    </style>
    """, unsafe_allow_html=True) 