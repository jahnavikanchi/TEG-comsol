import streamlit as st
import base64
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="COMSOL Simulation Results",
    layout="wide"
)



# -----------------------------
# Helpers
# -----------------------------
def load_image(image_file):
    image_file = Path(image_file)
    if not image_file.exists():
        return None
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()


def render_image(image_path, caption, width="70%"):
    image_base64 = load_image(image_path)

    if image_base64:
        st.markdown(
            f'''
            <div class="image-card">
                <img src="data:image/png;base64,{image_base64}" style="width:{width}; height:auto;">
                <div class="image-caption">{caption}</div>
            </div>
            ''',
            unsafe_allow_html=True
        )
    else:
        st.warning(f"Image not found: {image_path}")


def render_table(df):
    html_table = (
        '<div class="table-wrapper">'
        f'{df.to_html(index=False, escape=False, border=0, classes="custom-table")}'
        '</div>'
    )
    st.markdown(html_table, unsafe_allow_html=True)


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
    margin-bottom: 2rem;
}

.section-text {
    font-size: 1.05rem;
    line-height: 1.8;
    text-align: justify;
    color: #374151;
}

div[data-testid="stExpander"] {
    background: white;
    border-radius: 20px;
    border: 1px solid rgba(0,0,0,0.08);
    box-shadow: 0 8px 22px rgba(0,0,0,0.05);
    margin-bottom: 1.5rem;
}

div[data-testid="stExpander"] summary {
    font-size: 1.2rem;
    font-weight: 800;
    color: #12372A;
}

.custom-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
    margin: 1rem auto;
}

.custom-table th {
    background: #12372A;
    color: white;
    padding: 0.8rem;
    text-align: center;
}

.custom-table td {
    padding: 0.8rem;
    border: 1px solid #d9d9d9;
    text-align: center;
}

.custom-table tr:nth-child(even) {
    background: #f7f9fb;
}

.table-wrapper {
    overflow-x: auto;
    margin: 1rem 0 1.5rem 0;
}

.image-card {
    background: white;
    border-radius: 18px;
    padding: 1rem;
    margin: 1.5rem auto;
    text-align: center;
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
}

.image-card img {
    border-radius: 12px;
}

.image-caption {
    font-size: 0.9rem;
    font-weight: 700;
    margin-top: 0.7rem;
    color: #374151;
}
            
.intro-card {
    background: white;
    border-radius: 22px;
    padding: 2rem;
    margin: 0 auto 2rem auto;
    box-shadow: 0 10px 25px rgba(0,0,0,0.06), 0 4px 10px rgba(0,0,0,0.03);
    border: 1px solid rgba(0,0,0,0.04);
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Page Title
# -----------------------------
st.markdown(
    '<div class="main-title">Comsol Simulation Results of the Thermoelectric Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="intro-card">
        <div class="section-text">
        This page presents the COMSOL Multiphysics® simulation results for the thermoelectric generator models studied in this project. 
        The simulations were used to visualize the temperature distribution, electric potential, and electric field generated across the device under defined thermal boundary conditions.
        <br><br>
        These results help compare the theoretical calculations with numerical simulation outputs and provide insight into how geometry, material selection, and temperature gradient influence the final performance of the thermoelectric generator.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Shared Data Table
# -----------------------------
data = {
    "Component": ["Ohmic Contact", "Insulating Contact", "P-type Leg", "N-type Leg"],
    "Dimensions (m)": [
        "0.005 × 0.006 × 0.0005",
        "0.017 × 0.006 × 0.001",
        "0.005 × 0.005 × 0.01",
        "0.005 × 0.005 × 0.01"
    ]
}

df = pd.DataFrame(data)


# -----------------------------
# Expander 1
# -----------------------------
with st.expander("2. TEG unit couple with Ag$_2$Se", expanded=False):

    st.subheader("Resultant maximum power output combination")

    st.write(
        """Based on the findings from the "Optimal Pairings of Two Materials" section, the most suitable p-type material for pairing with Ag$_2$Se  in a thermoelectric generator (TEG) is SnS$_{0.91}$Se$_{0.09}$. This material combination was subsequently analyzed through simulations using the thermoelctric study module (stationary study) of COMSOL Multiphysics® software."""
    )

    st.write("""First the 3D model of the TEG was built with the following dimensions: """)

    render_table(df)

    render_image(
        "views/Comsol_simulation_images/Scales_.png",
        "Figure 1: Scales of the model",
        width="60%"
    )

    st.write(
        """Then, each component is assigned with it's respective material and it's respective properties such as thermal conductivity, seebeck coefficient, etc."""
    )

    render_image(
        "views/Comsol_simulation_images/Components_Labelled.png",
        "Figure 2: The assigned materials.",
        width="60%"
    )

    st.write(
        """Then the each the conditions to the respective domains or plains were assigned. For this particular simulation the bottom plane is assigned 399K which and the top plane is assigned 299K. Then the p-type ohmic contact is set to be a ground terminal and the n-type ohmic contact is assigned a voltage variable V."""
    )

    render_image(
        "views/Comsol_simulation_images/Conditions.png",
        "Figure 3: Figure showcasing the applied conditions to the respective planes.",
        width="60%"
    )

    st.write(
        """Finally, the simulation is computed. The results included a volumetric temperature gradient, electric field, and electric potential variation"""
    )

    render_image(
        "views/Comsol_simulation_images/Final_TempGrad_ag2se.png",
        "Figure 4: Temperature gradient of TEG.",
        width="70%"
    )

    st.write(
        """In figure 4, the temperature difference is 100K. This is the temperature range that we have selected for our material is between 299K-399K which is the same temperature range choosen for theoretical calculation as well."""
    )

    render_image(
        "views/Comsol_simulation_images/Final_Potential_ag2se.png",
        "Figure 5: Simulation of the electric potential gradient generated in TEG.",
        width="70%"
    )

    st.write(
        """From the figure 5, it's found that the the voltage difference that is generated is around 0.033V. From the theoretical calculations of the same TEG module, it was found to be which is about 10e-1 times the theoretically calculated value of voltage. This could be due to the length, which was taken 10e-1 times the original length.\n Power calculated here is 0.225W."""
    )

    render_image(
        "views/Comsol_simulation_images/Final_Field_ag2se.png",
        "Figure 6: Electric Field generated in TEG.",
        width="70%"
    )


# -----------------------------
# Expander 2
# -----------------------------
with st.expander("Maximum power ouput for the materials from the database", expanded=False):

    st.subheader("Maximum power output combination")

    st.write(
        """At this stage of the project, we transition from analytical calculations to numerical modeling of thermoelectric processes using the finite element method (FEM) in COMSOL Multiphysics. In the preveous part of the study, a simplified version of the problem was solved using analytical equations, allowing us to estimate key parameters of thermoelectric elements such as output power, voltage, and resistance. However, real-world engineering problems are often more complex and require advanced computational methods.

  The main purpose of this stage is to compare the analytical calculations obtained in the previous part with the results of numerical simulations in COMSOL, where the temperature dependences of the material properties obtained in the previous calculations based on the database are used as the main physical characteristics of the material. This approach will allow us to account for more complex physical interactions, such as the distribution of temperature and electric potential within the system, as well as the influence of geometry and material properties. 
  Here we present a couple of materials that have shown maximum power in the theoretical calculations.

  FeNb$_{0.92}$Ti$_{0.08}$Sb and Sr$_{0.21}$Yb$_{0.03}$Co$_{4}$Sb$_{12.12}$ with maximum power output of 60 mW and voltage of 23 mV.
  
  """
    )

    render_table(df)

    render_image(
        "views/Comsol_simulation_images/V_T1.png",
        "Figure 1: Volumic Temperaure distribution (K)",
        width="90%"
    )

    st.write(
        """We then considered the electric potential from which we took the voltage for further calculations of power. V=24.7 mV"""
    )

    render_image(
        "views/Comsol_simulation_images/V_electric_potential.png",
        "Figure 2: Electric potential (V)",
        width="90%"
    )

    st.write(
        """As a result of calculations of the maximum output power obtained by numerical simulation, we concluded that the results of the analytical calculation (60 mW) are slightly lower than the results obtained by simulation (70 mW). The voltage for this pair obtained by modeling is 24.7 mV, whereas it is 22.9 mV in the analytical calculations."""
    )


# -----------------------------
# Expander 3
# -----------------------------
with st.expander("Number of TEG Units Needed to Achieve 5V Output", expanded=False):

    st.subheader("15 TEG Units Needed to Achieve 5V Output")

    st.write(
        """Our objective was to design and manufacture a thermoelectric generator capable of producing the highest possible output power using thermocouples. The working principle was the same as that of a single manufactured thermocouple, but by combining it N times, we could achieve a total power sufficient to charge a Huawei Nova 7i smartphone. To maximize the output power and ensure optimal efficiency, the thermocouples needed to be arranged in series. This configuration allowed the voltages generated by each thermocouple to add up, ultimately reaching the required power level. """
    )

    render_table(df)

    render_image(
        "views/Comsol_simulation_images/D_T1.png",
        "Figure 1: Volumic Temperaure distribution (K)",
        width="60%"
    )

    render_image(
        "views/Comsol_simulation_images/D_T2.png",
        "Figure 1: Volumic Temperaure distribution (K)",
        width="60%"
    )

    st.write("""We then considered the electric fields""")

    render_image(
        "views/Comsol_simulation_images/D_electric_potential.png",
        "Figure 2: Electric potential (V)",
        width="60%"
    )

    st.write("""The distribution of the electric field is also considered""")

    render_image(
        "views/Comsol_simulation_images/D_electric_field.png",
        "Figure 3: Electric field distribution",
        width="60%"
    )