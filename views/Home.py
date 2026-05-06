import streamlit as st
import base64

#for making the background image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_jpg_as_page_bg(jpg_file):
    bin_str = get_base64_of_bin_file(jpg_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
#Backgroung image of home page
background_image_path = 'views/Images/Home_BG.jpg'

#setting the background image
set_jpg_as_page_bg(background_image_path)

#CSS styling 
st.markdown('''
    <style>
    body {
        color: white;  /* Text color */
        font-family: 'Times New Roman', sans-serif;  /* Default font */
    }
    h1 {
        font-family: 'Georgia', sans-serif;  /* Different font for headers */
        color: white; font-size: 50px; 
    }
    h2, h3 {
        font-family: 'Times New Roman', monospace;  /* Different font for headers */
        color: white; font-size: 40px;
    }
    .member-name {
        font-family: 'Times New Roman', serif;  /* Font for member names */
        font-size: 14px;  /* Size for member names */
    }
   .member-role {
        font-family: 'Times New Roman', sans-serif;  /* Font for member roles */
        font-size: 12px;  /* Size for member roles */
    }
    </style>
    ''', unsafe_allow_html=True)

st.write("<h1> Home </h1>", unsafe_allow_html=True)
# Contenu de votre application
st.write("""<h2>Group 1</h2>""", unsafe_allow_html=True)

st.write(""" FAMEAIS Energ'AI project 2024: Design of a thermoelectric energy harvesting device""")

st.write("<body>Harnessing Waste Heat, Powering the Future. </body>", unsafe_allow_html=True)