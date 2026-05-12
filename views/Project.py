import streamlit as st

st.set_page_config(
    page_title="Project Introduction",
    layout="wide"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #f7f9fb;
    color: #1f2937;
}

.hero-title {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 800;
    color: #12372A;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}

.hero-subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #526D5B;
    max-width: 900px;
    margin: 0 auto 3rem auto;
    line-height: 1.8;
}

.section-card {
    background: white;
    border-radius: 24px;
    padding: 2.2rem;
    margin: 0 auto 2rem auto;
    max-width: 1200px;

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
    line-height: 1.9;
    text-align: justify;
    color: #374151;
}

.highlight-card {
    background: linear-gradient(135deg, #12372A, #1D4D3F);
    color: white;
    border-radius: 24px;
    padding: 2.4rem;
    margin: 0 auto 2rem auto;
    max-width: 1200px;

    box-shadow:
        0 12px 28px rgba(18,55,42,0.25);
}

.highlight-title {
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 1rem;
}

.highlight-text {
    font-size: 1.05rem;
    line-height: 1.9;
    text-align: justify;
}

.stats-container {
    max-width: 1200px;
    margin: 0 auto 2rem auto;

    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
}

.stat-card {
    background: white;
    border-radius: 20px;
    padding: 1.5rem;
    text-align: center;

    box-shadow:
        0 6px 18px rgba(0,0,0,0.05);

    border: 1px solid rgba(0,0,0,0.04);
}

.stat-number {
    font-size: 2rem;
    font-weight: 800;
    color: #12372A;
}

.stat-label {
    color: #6B7280;
    margin-top: 0.5rem;
    font-size: 0.95rem;
}

@media screen and (max-width: 900px) {
    .hero-title {
        font-size: 2.5rem;
    }

    .section-card,
    .highlight-card {
        padding: 1.6rem;
    }

    .stats-container {
        grid-template-columns: 1fr 1fr;
    }
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# HERO
# -----------------------------
st.markdown("""
<div class="hero-title">Thermoelectric Generators</div>

<div class="hero-subtitle">
A data-driven project combining thermoelectric materials, geometry optimisation,
COMSOL Multiphysics simulations, and machine learning.
</div>
""", unsafe_allow_html=True)


# -----------------------------
# INTRODUCTION
# -----------------------------
st.markdown(
    '<div class="section-card">'
    '<div class="section-title">Project Introduction</div>'
    '<div class="section-text">'
    'Thermoelectric generators convert heat directly into electrical energy using '
    'temperature differences. This process is based on the Seebeck effect, where '
    'a voltage is generated when one side of a thermoelectric material is hotter '
    'than the other. Because thermoelectric devices do not require moving parts, '
    'they are compact, reliable, and suitable for sustainable energy conversion.'
    '<br><br>'
    'This technology is especially useful for recovering waste heat from industrial '
    'systems, electronic devices, engines, and wearable applications. Instead of '
    'losing heat to the environment, thermoelectric generators allow part of this '
    'thermal energy to be converted into usable electrical power.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# PROJECT DETAILS
# -----------------------------
st.markdown(
    '<div class="highlight-card">'
    '<div class="highlight-title">What This Project Is About</div>'
    '<div class="highlight-text">'
    'In this project, we focused on the geometric optimisation of a thermoelectric '
    'generator while keeping Ag₂Se as the n-type thermoelectric material.'
    '<br><br>'
    'Using Python, we generated around 5000 unique geometry combinations by varying '
    'important design parameters such as thermoelectric leg dimensions, interconnect '
    'dimensions, filling factor, material widths, contact resistivity, input heat '
    'flux density, and hot-side temperature.'
    '<br><br>'
    'These generated cases were then simulated in COMSOL Multiphysics using a '
    'parametric study. The simulation results were collected into a dataset and '
    'later used for machine learning-based geometric optimisation.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# STATS
# -----------------------------
st.markdown(
    '<div class="stats-container">'
    '<div class="stat-card">'
        '<div class="stat-number">5000</div>'
        '<div class="stat-label">Unique Geometry Cases</div>'
    '</div>'

    '<div class="stat-card">'
        '<div class="stat-number">Ag₂Se</div>'
        '<div class="stat-label">n-type Thermoelectric Material</div>'
    '</div>'

    '<div class="stat-card">'
        '<div class="stat-number">COMSOL</div>'
        '<div class="stat-label">Parametric Simulations</div>'
    '</div>'

    '<div class="stat-card">'
        '<div class="stat-number">ML</div>'
        '<div class="stat-label">Geometry Optimisation</div>'
    '</div>'
'</div>', unsafe_allow_html=True)


# -----------------------------
# WORKFLOW
# -----------------------------
st.markdown(
'<div class="section-card">'
    '<div class="section-title">Project Workflow</div>'

    '<div class="section-text">'
        'The project followed a computational workflow beginning with automated'
        'geometry generation using Python. Each design case represented a unique'
        'combination of geometric and operating parameters.'
        '<br><br>'
        'These cases were imported into COMSOL Multiphysics and evaluated through'
        'parametric simulations. The resulting performance data was then used to train'
        'machine learning models for predicting and optimising thermoelectric generator'
        'efficiency.'
        '<br><br>'
        'By combining simulation and machine learning, the project demonstrates a'
        'faster and more systematic approach to thermoelectric device design.'
    '</div>'
'</div>', unsafe_allow_html=True)


# -----------------------------
# FUTURE RELEVANCE
# -----------------------------
st.markdown(
'<div class="section-card">'
    '<div class="section-title">Why It Matters</div>'

    '<div class="section-text">'
        'Thermoelectric generators offer a promising route for sustainable energy'
        'recovery, especially in systems where waste heat is readily available.'
        ' Improving their geometry can directly influence device efficiency and practical'
        'performance.'
        '<br><br>'
        'This project shows how materials science, numerical simulation, and machine'
        'learning can work together to accelerate the design of efficient energy'
        'conversion devices.'
    '</div>'
'</div>', unsafe_allow_html=True)