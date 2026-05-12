import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components

st.set_page_config(page_title="Our Material", layout="wide")


# -----------------------------
# Helpers
# -----------------------------
def img_to_base64(path):
    path = Path(path)
    if not path.exists():
        return None
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


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
    font-size: 3rem;
    font-weight: 900;
    color: #12372A;
    margin-bottom: 1rem;
}

.main-subtitle {
    font-size: 1.05rem;
    line-height: 1.7;
    text-align: justify;
    margin-bottom: 2rem;
    color: #111827;
}

.card {
    background: white;
    border-radius: 14px;
    padding: 1rem;
    margin-bottom: 1rem;
    border: 1px solid #d9d9d9;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
}

.card-title {
    font-size: 1.6rem;
    font-weight: 800;
    color: #12372A;
    margin-bottom: 0.8rem;
}

.section-text {
    font-size: 1rem;
    line-height: 1.65;
    text-align: justify;
    color: #111827;
}

.source-line {
    font-size: 1rem;
    margin-bottom: 0.8rem;
}

.source-line a {
    color: #1D4ED8;
    font-weight: 700;
    text-decoration: none;
}

.viewer-box {
    border: 1px solid #d1d5db;
    border-radius: 8px;
    overflow: hidden;
    background: white;
}

.legend {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 0.8rem;
    font-weight: 700;
}

.legend-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.dot {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    display: inline-block;
}

.dot-ag {
    background: #BDBDBD;
    border: 1px solid #999;
}

.dot-se {
    background: #7CFC00;
    border: 1px solid #65B800;
}

.material-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 1rem;
}

.material-table th {
    background: #12372A;
    color: white;
    padding: 0.7rem;
    text-align: left;
}

.material-table td {
    padding: 0.7rem;
    border: 1px solid #d9d9d9;
}

.material-table tr:nth-child(even) {
    background: #f7f9fb;
}

.formula-box {
    text-align: center;
    font-size: 1.5rem;
    margin-top: 1rem;
}

.bottom-source {
    text-align: center;
    background: #eef2ef;
    padding: 0.8rem;
    border-radius: 0 0 10px 10px;
    font-weight: 700;
}

.bottom-source a {
    color: #1D4ED8;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="main-title">Ag₂Se: A Promising Thermoelectric Material</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="main-subtitle">'
    'Silver selenide (Ag₂Se) is a highly efficient thermoelectric material, particularly for applications near room temperature. '
    'Its unique combination of electrical and thermal properties, coupled with its phase transition behavior, makes it an ideal candidate for energy conversion and waste heat recovery. '
    'Below is an overview of its thermoelectric properties, phase transitions, and mechanisms that drive its performance.'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Crystal + Tables Row
# -----------------------------
left_col, right_col = st.columns([1.7, 1], gap="medium")

with left_col:
    st.markdown(
        '<div class="card">'
        '<div class="card-title">Crystal Structure</div>'
        '<div class="source-line">'
        '<b>Source:</b> '
        '<a href="https://next-gen.materialsproject.org/" target="_blank">Materials Project</a>'
        ' &nbsp; | &nbsp; '
        '<a href="https://next-gen.materialsproject.org/materials/mp-754954?formula=Ag2Se" target="_blank">View Material on Materials Project ↗</a>'
        '</div>',
        unsafe_allow_html=True
    )

    cif_path = Path("views/structures/Ag2Se.cif")

    if cif_path.exists():
        cif_data = cif_path.read_text().replace("`", "\\`")

        viewer_html = f"""
        <div class="viewer-box">
            <div id="viewer" style="width:100%; height:440px; position:relative;"></div>
        </div>

        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>

        <script>
            let element = document.getElementById("viewer");
            let viewer = $3Dmol.createViewer(element, {{ backgroundColor: "white" }});

            let cifData = `{cif_data}`;
            viewer.addModel(cifData, "cif");

            viewer.setStyle({{elem: "Ag"}}, {{
                sphere: {{ scale: 0.35, color: "#BDBDBD" }},
                stick: {{ radius: 0.12, color: "#BDBDBD" }}
            }});

            viewer.setStyle({{elem: "Se"}}, {{
                sphere: {{ scale: 0.35, color: "#7CFC00" }},
                stick: {{ radius: 0.12, color: "#7CFC00" }}
            }});

            viewer.addUnitCell();
            viewer.zoomTo();
            viewer.render();
        </script>
        """

        components.html(viewer_html, height=470)

    else:
        image_base64 = img_to_base64("views/Images/Crystall_sructure.png")
        if image_base64:
            st.markdown(
                f'<img src="data:image/png;base64,{image_base64}" style="width:100%; border-radius:8px; border:1px solid #d1d5db;">',
                unsafe_allow_html=True
            )
        else:
            st.warning("Add views/Structures/Ag2Se.cif or views/Images/Crystall_sructure.png")

    st.markdown(
        '<div class="legend">'
        '<div class="legend-item"><span class="dot dot-ag"></span>Ag⁺</div>'
        '<div class="legend-item"><span class="dot dot-se"></span>Se²⁻</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with right_col:
    st.markdown(
        '<div class="card">'
        '<div class="card-title">Lattice (Conventional)</div>'
        '<table class="material-table">'
        '<tr><th>Parameter</th><th>Value</th></tr>'
        '<tr><td>a</td><td>4.68 Å</td></tr>'
        '<tr><td>b</td><td>7.39 Å</td></tr>'
        '<tr><td>c</td><td>7.8 Å</td></tr>'
        '<tr><td>α</td><td>90°</td></tr>'
        '<tr><td>β</td><td>90°</td></tr>'
        '<tr><td>γ</td><td>90°</td></tr>'
        '<tr><td><b>Volume</b></td><td><b>264.64 Å³</b></td></tr>'
        '</table>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card">'
        '<div class="card-title">Symmetry</div>'
        '<table class="material-table">'
        '<tr><th>Property</th><th>Value</th></tr>'
        '<tr><td>Crystal System</td><td>Orthorhombic</td></tr>'
        '<tr><td>Space group</td><td><i>P</i>2₁2₁2₁</td></tr>'
        '<tr><td>Point Group</td><td>222</td></tr>'
        '</table>'
        '</div>',
        unsafe_allow_html=True
    )


# -----------------------------
# Content Sections
# -----------------------------
st.markdown(
    '<div class="card">'
    '<div class="card-title">Thermoelectric Properties of Ag₂Se</div>'
    '<div class="section-text">'
    '<b>Ag₂Se</b>, a promising n-type chalcogenide material, has garnered attention as an ideal candidate for room-temperature thermoelectric applications due to its low thermal conductivity '
    '(k<sub>total</sub> ≈ 1 W/m·K) and narrow band gap (0.04–0.2 eV). These characteristics contribute to a high S²/ρ figure of merit at room temperature, making '
    '<b>Ag₂Se</b> highly suitable for energy conversion and waste-heat recovery technologies [6].'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card">'
    '<div class="card-title">Phase Transition and Superionic Behavior</div>'
    '<div class="section-text">'
    'Ag₂Se undergoes a significant phase transition from a semiconducting <b>orthorhombic phase</b> to a superionic <b>cubic phase</b> at approximately 407 K. '
    'In the cubic phase, silver ions (Ag⁺) become highly mobile within a rigid selenium lattice. This transition results in metallic conduction and superionic characteristics, '
    'which are crucial for enhancing thermoelectric performance. However, the low-temperature orthorhombic phase, while showing promising thermoelectric behavior, is limited by inconsistent '
    '<i>ZT</i> values ranging from 0.3 to 0.96 in the 300–400 K range [7].'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card">'
    '<div class="card-title">Achieving High Thermoelectric Performance</div>'
    '<div class="section-text">'
    'Recent advancements have demonstrated a significant improvement in the thermoelectric performance of <b>Ag₂Se</b>, achieving <i>ZT</i> values between 0.9 and 1.0 over the 300–375 K range. '
    'This highlights <b>n-type bulk Ag₂Se</b> as a competitive material in comparison to state-of-the-art low-temperature thermoelectric materials. '
    'The high carrier mobility and low lattice thermal conductivity (0.2–0.1 W/m·K) contribute to its efficiency in converting heat to electricity, even at low temperature differences, such as 80 K [8].'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card">'
    '<div class="card-title">Challenges in Achieving Consistent <i>ZT</i></div>'
    '<div class="section-text">'
    'One of the main challenges facing the widespread use of <b>Ag₂Se</b> in thermoelectric applications is the inconsistency in its figure of merit (<i>ZT</i>) due to an unoptimized crystal structure and chemical composition. '
    'Recent studies have proposed strategies to stabilize the orthorhombic phase and improve carrier mobility by enhancing the material’s defect structure, which can lead to up to a 70% increase in mobility. '
    'Additionally, controlling impurities and optimizing the defect structure have been shown to reduce contact resistance, further enhancing the material’s efficiency in thermoelectric devices [9].'
    '</div>'
    '<div class="formula-box"><i>ZT</i> = S²σT / k</div>'
    '</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Heat Sources
# -----------------------------
st.markdown(
    '<div class="card">'
    '<div class="card-title">Suitable Heat Sources for Ag₂Se</div>'
    '<div class="section-text">'
    '<b>Ag₂Se</b> is an ideal material for converting heat into electricity, particularly when exposed to heat sources in the <b>300 K to 400 K</b> range. Suitable heat sources include:'
    '</div>'
    '<br>'
    '<table class="material-table">'
    '<tr><th>Heat Source</th><th>Description</th></tr>'
    '<tr><td><b>Industrial Waste Heat</b></td><td>Many industrial processes, such as steel and cement production, release heat in the 200°C to 400°C range, which can be harnessed by Ag₂Se for thermoelectric generation.</td></tr>'
    '<tr><td><b>Automotive Exhaust</b></td><td>Exhaust gases from vehicles, typically in the 150°C to 500°C range, provide a reliable source of heat for Ag₂Se thermoelectric modules.</td></tr>'
    '<tr><td><b>Solar Thermal Collectors</b></td><td>These systems capture solar energy, operating within the 100°C to 300°C range, making them ideal for use with Ag₂Se in solar energy applications.</td></tr>'
    '<tr><td><b>Geothermal Energy</b></td><td>Geothermal heat, typically between 150°C to 300°C, offers a steady and renewable heat source that Ag₂Se can convert into electrical energy.</td></tr>'
    '</table>',
    unsafe_allow_html=True
)