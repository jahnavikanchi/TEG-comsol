import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE SETUP---
about_page=st.Page(
    page="views/Home.py",
    title="Home",
    default=True,
)
project_1_page=st.Page(
    page="views/Project.py",
    title="Project Introduction",
   
)
project_2_page=st.Page(
    page="views/About_Us.py",
    title="About Us",
   
)

project_3_page=st.Page(
    page="views/Resources.py",
    title="Resources",
    
)

project_4_page=st.Page(
    page="views/Our_Material.py",
    title="Our Material: Ag₂Se",
)

    
project_5_page=st.Page(
    page="views/Optimal pairings of two materials.py",
    title="Optimal pairings of two materials",
    
)

project_6_page=st.Page(
    page="views/Comsol_results.py",
    title="Comsol Simulation Results",
)

project_7_page=st.Page(
    page="views/comsol 5000.py",
    title="Dataset: 5K Cases Simulation",
)



project_8_page = st.Page(
    page="views/ML_Results.py",
    title="ML Results",
)

#--- NAVIGATION SETUP [WITHOUT SECTIONS]---


#--- NAVIGATION SETUP [WITHOUT SECTIONS]---
#--- NAVIGATION SETUP [WITHOUT SECTIONS]---
pg = st.navigation(
    {"Info" :[about_page, project_2_page], 
    "Introduction" : [project_1_page, project_4_page],
    "Theoretical foundations" : [project_5_page, project_6_page],
    "Machine Learning" : [project_7_page, project_8_page],
    "Resources" : [project_3_page],
    }
)





# --- RUN NAVIGATION ---
pg.run()


# --- STYLE & POLICE ---
st.markdown('''
    <style>
    body {
        color: white;  /* Text color */
        font-family: 'Georgia', sans-serif;  /* Default font */
    }
    h1 {
        font-family: 'Georgia', sans-serif;  /* Different font for headers */
        color: white; font-size: 50px; 
    }
    h2, {
        font-family: 'Times New Roman', monospace;  /* Different font for headers */
        color: white; font-size: 50px;
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

import os 
os.write(1,b'Home was executed.\n')

