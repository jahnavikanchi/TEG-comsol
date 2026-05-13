import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="5000 Cases Simulation", layout="wide")


# -----------------------------
# Helpers
# -----------------------------
def load_image(image_file):
    image_file = Path(image_file)
    if not image_file.exists():
        return None

    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()


def render_card(title, body):
    st.markdown(
        f'<div class="content-card">'
        f'<div class="section-title">{title}</div>'
        f'<div class="section-text">{body}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


def render_image(image_path, caption):
    image_base64 = load_image(image_path)

    if image_base64:
        st.markdown(
            f'<div class="image-card">'
            f'<img src="data:image/png;base64,{image_base64}" class="main-image">'
            f'<div class="image-caption">{caption}</div>'
            f'</div>',
            unsafe_allow_html=True
        )
    else:
        st.warning(f"Image not found: {image_path}")


# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: #f7f9fb;
    color: #1f2937;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

.main-title {
    text-align: center;
    font-size: 3.2rem;
    font-weight: 900;
    color: #12372A;
    margin-bottom: 0.8rem;
}

.main-subtitle {
    text-align: center;
    font-size: 1.15rem;
    color: #526D5B;
    margin-bottom: 2.5rem;
}

.content-card {
    background: white;
    border-radius: 24px;
    padding: 2.2rem;
    margin-bottom: 1.8rem;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.06),
        0 4px 10px rgba(0,0,0,0.03);

    border: 1px solid rgba(0,0,0,0.04);
}

.section-title {
    font-size: 2rem;
    font-weight: 800;
    color: #12372A;
    margin-bottom: 1rem;
}

.section-text {
    font-size: 1.05rem;
    line-height: 1.85;
    text-align: justify;
    color: #374151;
}

.section-text a {
    color: #1D4ED8;
    font-weight: 700;
    text-decoration: none;
}

.image-card {
    background: white;
    border-radius: 24px;
    padding: 1.5rem;
    margin-bottom: 1.8rem;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.06),
        0 4px 10px rgba(0,0,0,0.03);

    border: 1px solid rgba(0,0,0,0.04);

    text-align: center;
}

.main-image {
    width: 100%;
    border-radius: 18px;
}

.image-caption {
    font-size: 0.95rem;
    line-height: 1.6;
    color: #374151;
    font-weight: 600;
    margin-top: 1rem;
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="main-title">5000 Cases Simulation</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="main-subtitle">Python-generated geometry cases, COMSOL simulations, and result extraction workflow</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Section 1
# -----------------------------
render_card(
    "1. Generating Case Parameters",
    'The parameters such as the height of the thermoelectric leg, the height of the interconnects, hot side temperature, etc... were generated using python. '
    'The parameter values were generated based on specific criteria and subjected to predefined constraints to ensure validity and relevance. These values were then stored in a CSV file, which serves as the foundation for constructing the dataset used in subsequent analysis or modeling. '
    '<a href="https://colab.research.google.com/drive/1DfcdirBFgdQxCMptFk3BuDq6BVCpin_b?usp=sharing" target="_blank">[Colab File]</a>'
)

render_image(
    "views/Images/histogram.png",
    "Fig 1: The histogram depicts the value spread of the parameters data generated.The x-axis represents the parameter values, while the y-axis indicates the frequency of each value. This visualization provides insights into the range and distribution of the generated parameters, helping to identify any potential biases or anomalies in the data generation process."
)


# -----------------------------
# Section 2
# -----------------------------
render_card(
    "2. Finding a Polynomial as a Function of Temperature",
    'The polynomial function was generated using the numpy library in Python. The coefficients of the polynomial were determined through a fitting process. The generated polynomial function can be used for further analysis or modeling tasks. '
    '<a href="https://colab.research.google.com/drive/1GrvoyQqBbBhPa4e7cMgTDY4QXbsX4PPH?usp=sharing" target="_blank">[Colab File]</a>'
)


# -----------------------------
# Section 3
# -----------------------------
render_card(
    "3. Simulating Each Case",
    'The simulation was performed using the COMSOL Multiphysics software. It was found that there were different ways to go about simulating 5K differnt cases, first one being parametric sweep in one comsol file, second is using Matlab, and the last is using simple python.'
    '<br><br>'
    'We chose the last option which is using python. For this partcular method, it\'s required to generate a .txt file for each input, hence using another python code, generated about 5000 geometry case files, gave them as input and simulated each case, generating .mph file for each.'
)

render_card(
    "Simulation Workflow",
    'So, the first step is to create a template file with the respective variables set in the global parameters and initialise them with a random value, and simulate it, and then use this as a template file for the 5k cases.'
    '<br><br>'
    'The example .txt file is uploaded in the loop folder of the repositary. The python code used for the simulations has also been uploaded into the loop folder.'
    '<br><br>'
    'For each case it took about 50sec of simulation time. So, total simulation time took about 39 hrs.'
)

render_card(
    "Result Extraction",
    'It was after the simulation we realised the the export of each case is not being done, but each case generated had a .mph file respective to it\'s parameters and the computation has been performed successfully.'
    )