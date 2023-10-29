import streamlit as st

st.set_page_config(
    page_title="About Ni He",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.header('NI HE')

#side bar
st.sidebar.image("nihe_photo.jpg",caption="Developed and Maintaned by: nihe: nihe78@gmail.com")