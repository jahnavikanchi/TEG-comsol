import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Home",
    layout="wide"
)

# -----------------------------
# Helper
# -----------------------------
def img_to_base64(path):
    path = Path(path)
    if not path.exists():
        return None

    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# -----------------------------
# Background Image
# -----------------------------
background_image_path = "views/Images/Home_BG.jpg"
bg_base64 = img_to_base64(background_image_path)

if bg_base64:
    background_css = f"""
    <style>
    .stApp {{
        background-image:
            linear-gradient(
                rgba(10, 25, 20, 0.72),
                rgba(10, 25, 20, 0.72)
            ),
            url("data:image/jpg;base64,{bg_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)


# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

.block-container {
    padding-top: 8rem;
    padding-bottom: 4rem;
}

.hero-card {
    max-width: 1000px;
    margin: auto;

    padding: 4rem 3rem;

    border-radius: 30px;

    background: rgba(255, 255, 255, 0.10);

    border: 1px solid rgba(255, 255, 255, 0.22);

    box-shadow:
        0 20px 45px rgba(0,0,0,0.28);

    backdrop-filter: blur(8px);

    text-align: center;
}

.project-label {
    color: #CDE8D5;
    font-size: 1.1rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 1rem;
}

.hero-title {
    color: white;
    font-size: 4.4rem;
    font-weight: 900;
    line-height: 1.05;
    margin-bottom: 1.2rem;
}

.hero-subtitle {
    color: #F3F7F4;
    font-size: 1.35rem;
    line-height: 1.8;
    max-width: 800px;
    margin: auto;
}

.hero-tagline {
    margin-top: 2rem;

    display: inline-block;

    padding: 0.9rem 1.4rem;

    border-radius: 999px;

    background: rgba(255, 255, 255, 0.16);

    color: white;

    font-size: 1.1rem;
    font-weight: 700;
}

.nav-section {
    max-width: 1100px;
    margin: 2.5rem auto 0 auto;
}
            
div[data-testid="column"] {
    display: flex;
    flex-direction: column;
}

div[data-testid="stPageLink"] {
    width: 100% !important;
    min-width: 100% !important;
    box-sizing: border-box;

    background: rgba(255, 255, 255, 0.14);
    border: 1px solid rgba(255, 255, 255, 0.22);
    border-radius: 24px;

    padding: 1.6rem 1.2rem;
    min-height: 120px;

    backdrop-filter: blur(8px);

    display: flex;
    align-items: center;
    justify-content: center;

    text-align: center;

    transition: all 0.3s ease;
}

div[data-testid="stPageLink"]:hover {
    transform: translateY(-6px);
    background: rgba(255, 255, 255, 0.22);
    box-shadow: 0 10px 24px rgba(0,0,0,0.20);
}

div[data-testid="stPageLink"] a {
    width: 100% !important;
    height: 100% !important;

    display: flex !important;
    align-items: center !important;
    justify-content: center !important;

    color: white !important;
    font-size: 1.55rem !important;
    font-weight: 800 !important;
    text-decoration: none !important;
}
.nav-card-text {
    color: #E6EFE9;
    text-align: center;
    margin-top: 0.8rem;
    font-size: 1rem;
    line-height: 1.6;
    padding: 0 0.5rem;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Home Content
# -----------------------------
st.markdown(
    '<div class="hero-card">'
    '<div class="project-label">FAMEAIS Energ&apos;AI Project 2024 · Group 1</div>'
    '<div class="hero-title">Thermoelectric Energy Harvesting</div>'
    '<div class="hero-subtitle">'
    'Designing and optimising a thermoelectric energy harvesting device '
    'through geometry generation, COMSOL Multiphysics simulations, and machine learning.'
    '</div>'
    '<div class="hero-tagline">Harnessing Waste Heat, Powering the Future.</div>'
    '</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Navigation Cards
# -----------------------------
st.markdown('<div class="nav-section">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1], gap="medium")

with col1:
    st.page_link(
        "views/Our_Material.py",
        label="Our Material: Ag₂Se",
    )

    st.markdown(
        '<div class="nav-card-text">'
        'n-type thermoelectric material used in the device design.'
        '</div>',
        unsafe_allow_html=True
    )

with col2:
    st.page_link(
        "views/Project.py",
        label="About Project",
    )

    st.markdown(
        '<div class="nav-card-text">'
        'Unique geometry combinations generated using Python.'
        '</div>',
        unsafe_allow_html=True
    )

with col3:
    st.page_link(
        "views/ML_Results.py",
        label="ML Optimisation",
    )

    st.markdown(
        '<div class="nav-card-text">'
        'Simulation results used for data-driven geometry optimisation.'
        '</div>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)