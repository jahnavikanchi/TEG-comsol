import streamlit as st

st.set_page_config(
    page_title="Resources",
    layout="wide"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp {
    background: #f7f9fb;
    color: #1f2937;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 4rem;
    max-width: 1200px;
}

.page-title {
    text-align: center;
    font-size: 3.4rem;
    font-weight: 900;
    color: #12372A;
    margin-bottom: 0.5rem;
}

.page-subtitle {
    text-align: center;
    font-size: 1.15rem;
    color: #526D5B;
    margin-bottom: 3rem;
}

.resource-card {
    background: white;

    border-radius: 24px;

    padding: 2rem;

    margin-bottom: 1.8rem;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.06);

    border: 1px solid rgba(0,0,0,0.05);
}

.section-title {
    font-size: 1.8rem;
    font-weight: 800;
    color: #12372A;
    margin-bottom: 1.5rem;
}

.resource-item {
    padding: 1rem 1.2rem;

    border-radius: 16px;

    margin-bottom: 1rem;

    background: #f8fbf9;

    border-left: 5px solid #4F6F52;

    transition: all 0.25s ease;
}

.resource-item:hover {
    transform: translateX(4px);
    background: #eef5f1;
}

.resource-item a {
    color: #12372A !important;
    text-decoration: none !important;
    font-weight: 600;
}

.resource-item a:hover {
    text-decoration: underline !important;
}

.footer-note {
    margin-top: 2rem;

    padding: 1.5rem;

    border-radius: 18px;

    background: rgba(18, 55, 42, 0.06);

    color: #374151;

    text-align: center;

    font-size: 0.98rem;

    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="page-title">Resources</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="page-subtitle">'
    'Research articles, databases, simulation tools, and project resources used throughout the study.'
    '</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Articles
# -----------------------------

references = [
    "[1] Sun et al., Pushing thermoelectric generators toward energy harvesting from the human body: Challenges and strategies, Materials Today 57, 121-145 (2022) https://doi.org/10.1016/j.mattod.2022.06.001",

    "[2] Wu et al., Thermoelectric converter: Strategies from materials to device application, Nano Energy 91, 106692 (2022). https://doi.org/10.1016/j.nanoen.2021.106692",

    "[3] Zhang et al., Flexible thermoelectric materials and devices: From materials to applications, Materials Today 46, 62-108 (2021). https://doi.org/10.1016/j.mattod.2021.02.016",

    "[4] Sanad et al., Thermoelectric Energy Harvesters: A Review of Recent Developments in Materials and Devices for Different Potential Applications, Topics in Current Chemistry 378, 48 (2020). https://doi.org/10.1007/s41061-020-00310-w",

    "[5] Petsagkourakis et al., Thermoelectric materials and applications for energy harvesting power generation, Science and Technology of Advanced Materials 19, 836-862 (2018). https://doi.org/10.1080/14686996.2018.1530938",

    "[6] Zhang, Jin, et al., High-Performance Flexible Supercapacitors Based on Mesoporous NiCo2S4 Nanosheets and Nanowire-Entangled Multiwalled Carbon Nanotube Networks. Journal of Materials Chemistry A 8, no. 28 (2020): 14017-14028. https://doi.org/10.1039/D0TA02614J",

    "[7] Mathew, Tony & Vaiyapuri, Vijay & Archana, J. & M., Navaneethan & Udaiyar, Ponnusamy. (2024). Tailoring the Lattice Thermal Conductivity of Al‐Incorporated Ag2Se for Near Room Temperature Waste Heat Recovery. ChemNanoMat. http://dx.doi.org/10.1002/cnma.202400298",

    "[8] Liu, M., Zhang, X., Zhang, S. et al. Ag2Se as a tougher alternative to n-type Bi2Te3 thermoelectrics. Nat Commun 15, 6580 (2024). https://doi.org/10.1038/s41467-024-50898-6",

    "[9] Ferhat, Marhoun, and Jiro Nagao., Thermoelectric and Transport Properties of β-Ag2Se Compounds. Journal of Applied Physics 88, no. 2 (2000). https://doi.org/10.1063/1.373741"
]

references_html = ""

for ref in references:
    references_html += f'''
    <div class="resource-item">
        {ref}
    </div>
    '''

st.markdown(
    f'''
    <div class="resource-card">
        <div class="section-title">Articles & References</div>
        {references_html}
    </div>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Project Resources</div>',
    unsafe_allow_html=True
)

project_resources = [
    '[10] <a href="https://github.com/KRICT-DATA/SIMD" target="_blank">SIMD Thermoelectric Database Repository</a>',

    '[11] <a href="https://colab.research.google.com/drive/19KxsuC8Po4ldIN2T20bF2U3q8ePTBeXo?usp=sharing" target="_blank">Python File — TEG Unit Couple Calculations</a>',

    '[12] COMSOL Multiphysics® COMSOL AB, Stockholm, Sweden. https://www.comsol.com'
]

for item in project_resources:
    st.markdown(
        f'<div class="resource-item">{item}</div>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <div class="footer-note">
    Acknowledgement of the use of
    <a href="https://chatgpt.com/c/67238468-d314-8003-a1bb-13921dd682bc" target="_blank">
    ChatGPT
    </a>
    for website design. All technical content and interpretations remain the responsibility of the authors.
    </div>
    """,
    unsafe_allow_html=True
)