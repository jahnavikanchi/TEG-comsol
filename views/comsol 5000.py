import streamlit as st
import pandas as pd
import numpy as np
import base64


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

st.write("<h1>5000 Cases Simulation</h1>", unsafe_allow_html=True)
st.write("<h2>1. Generating case parameters</h2>", unsafe_allow_html=True)

st.write("The parameters such as the height of the thermoelectric leg, the height of the interconnects, hot side temperature, etc... were generated using python." \
"The parameter values were generated based on specific criteria and subjected to predefined constraints to ensure validity and relevance. These values were then stored in a CSV file, which serves as the foundation for constructing the dataset used in subsequent analysis or modeling. [[Colab File]](https://colab.research.google.com/drive/1DfcdirBFgdQxCMptFk3BuDq6BVCpin_b?usp=sharing)" )

st.write("")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def load_image(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

hist_path = "views/Images/histogram.png"
image_base64 = load_image(hist_path)

if image_base64:
    st.markdown(f'<img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:100%;">', unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;font-size: 16px;'>Fig 1: The histogram depicts the value spread of the parameters data generated.The x-axis represents the parameter values, while the y-axis indicates the frequency of each value. This visualization provides insights into the range and distribution of the generated parameters, helping to identify any potential biases or anomalies in the data generation process.</h3>", unsafe_allow_html=True)


st.write("<h2>2. Finding a polynomial as a funciton of temperature</h2>", unsafe_allow_html=True)

st.write("The polynomial function was generated using the numpy library in Python. The coefficients of the polynomial were determined through a fitting process. The generated polynomial function can be used for further analysis or modeling tasks. [[Colab File]](https://colab.research.google.com/drive/1GrvoyQqBbBhPa4e7cMgTDY4QXbsX4PPH?usp=sharing)" )

st.write("<h2>3. Simulating each case</h2>", unsafe_allow_html=True)

st.write("The simulation was performed using the COMSOL Multiphysics software. It was found that there were different ways to go about simulating 5K differnt cases, first one being parametric sweep in one comsol file, second is using Matlab, and the last is using simple python." \
"\nWe chose the last option which is using python. For this partcular method, it's required to generate a .txt file for each input, hence using another python code, generated about 5000  geometry case files, gave them as input and simulated each case, generating .mph file for each.\n"
)

st.write("So, the first step is to create a template file with the respective variables set in the global parameters and initialise them with a random value, and simulate it, and then use this as a template file for the 5k cases.\n" \
"The example .txt file is uploaded in the loop folder of the repositary. The python code used for the simulations has also been uploaded into the loop folder." \
"For each case it took about 50sec of simulation time. So, total simulation time took about 39 hrs." \
"", unsafe_allow_html=True)


st.write("\nIt was after the simulation we realised the the export of each case is not being done, but each case generated had a .mph file respective to it's parameters and the computation has been performed successfully.")

st.write("So, at this point we decided to utilise matlab to extract the results from each .mph file, as it's mentioned that comsol files can be loaded in matlab via COMSOL LiveLink")