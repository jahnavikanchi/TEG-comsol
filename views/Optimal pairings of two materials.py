import streamlit as st
import pandas as pd

st.set_page_config(page_title="Optimizing Thermoelectric Devices", layout="wide")

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
            
.hero-title {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 800;
    color: #12372A;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}

.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 900;
    color: #12372A;
    margin-bottom: 1.5rem;
}

.intro-card, .content-card {
    background: white;
    border-radius: 22px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.06), 0 4px 10px rgba(0,0,0,0.03);
    border: 1px solid rgba(0,0,0,0.04);
}

.section-text {
    font-size: 1.05rem;
    line-height: 1.8;
    text-align: justify;
    color: #374151;
}

.section-title {
    font-size: 1.8rem;
    font-weight: 800;
    color: #12372A;
    margin-bottom: 1rem;
}

.small-title {
    font-size: 1.35rem;
    font-weight: 800;
    color: #12372A;
    margin-top: 1.5rem;
    margin-bottom: 0.8rem;
}

.custom-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}

.custom-table th {
    background: #12372A;
    color: white;
    padding: 0.75rem;
    text-align: left;
}

.custom-table td {
    padding: 0.75rem;
    border: 1px solid #d9d9d9;
}

.custom-table tr:nth-child(even) {
    background: #f7f9fb;
}

.table-caption {
    text-align: center;
    font-size: 0.85rem;
    font-weight: 700;
    color: #374151;
    margin-bottom: 1rem;
}

div[data-testid="stExpander"] {
    background: white;
    border-radius: 18px;
    border: 1px solid rgba(0,0,0,0.08);
    box-shadow: 0 6px 18px rgba(0,0,0,0.04);
    margin-bottom: 1.3rem;
}

div[data-testid="stExpander"] summary {
    font-size: 1.2rem;
    font-weight: 800;
    color: #12372A;
}

a {
    color: #1D4ED8;
    font-weight: 700;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Helper Functions
# -----------------------------
def format_subscripts(value):
    return value.replace('$_{', '<sub>').replace('}$', '</sub>')


def render_html_table(df, caption=None):
    df_html = df.copy()

    for col in df_html.columns:
        if df_html[col].dtype == object:
            df_html[col] = df_html[col].map(
                lambda x: format_subscripts(x) if isinstance(x, str) else x
            )

    df_html.index = df_html.index + 1

    html_table = (
        '<div style="overflow-x:auto;">'
        f'{df_html.to_html(index=True, escape=False, border=0, classes="custom-table")}'
        '</div>'
    )

    if caption:
        html_table += f'<div class="table-caption">{caption}</div>'

    st.markdown(html_table, unsafe_allow_html=True)


def display_image_grid(image_paths_top, image_paths_bottom, ratio=1.2):
    col1, col2 = st.columns([1, ratio])

    with col1:
        for img in image_paths_top:
            st.image(img, use_container_width=True)

    with col2:
        for img in image_paths_bottom:
            st.image(img, use_container_width=True)


# -----------------------------
# Title and Introduction
# -----------------------------
st.markdown('<div class="hero-title">Optimizing Thermoelectric Devices</div>', unsafe_allow_html=True)

st.markdown("""
<div class="intro-card">
<div class="section-text">
Thermoelectric materials offer a sustainable way to convert heat into electricity. This section focuses on optimizing the geometry of a thermoelectric device using silver selenide material to maximize power output.
<br><br>
Thermoelectric materials have garnered significant attention for their ability to directly convert heat into electricity, offering a sustainable and efficient means of energy generation. The performance of thermoelectric devices depends not only on the individual properties of the materials but also on the synergy between them when used in combination. In this part, we shift our focus from the initially assigned thermoelectric material to exploring optimal pairings of two materials from the provided database. The goal is to identify the combination that yields the highest power output, leveraging complementary thermoelectric properties such as Seebeck coefficient (α), electrical conductivity (σ), and thermal conductivity (k). This exercise highlights the importance of material compatibility and optimization in advancing thermoelectric technology for real-world applications.
<br><br>
The data for this analysis is sourced from the comprehensive thermoelectric materials database <a href="https://github.com/KRICT-DATA/SIMD" target="_blank">[10]</a>, which provides key material properties such as Seebeck coefficient (α), electrical conductivity (σ), and thermal conductivity (κ).
</div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Optimization Details and Results
# -----------------------------
with st.expander("Optimization Details and Results", expanded=False):
    st.markdown('<div class="section-title">Steps to Optimization</div>', unsafe_allow_html=True)

    st.markdown("""
    1. **Material Properties:** The average Seebeck coefficient (α)**, electrical conductivity (σ)**, and thermal conductivity ($\\Kappa$)** were calculated from the database.
    """)

    st.latex(r"V = \alpha \cdot \Delta T")

    st.markdown("2. **Resistance Calculation:**")
    st.latex(r"R = \rho \cdot \frac{L}{A}")
    st.markdown("where:")
    st.latex(r"\rho = \frac{1}{\sigma}")

    st.markdown("3. **Current and Power Output:**")
    st.latex(r"I = \frac{V}{2R}")
    st.latex(r"P = \frac{V^2}{4R}")

    st.markdown("""
    4. **Geometry Optimization:** By varying length (L)** and cross-sectional area (A)**, optimal designs were identified that balance electrical and thermal performance.

    ### Justification of Parameters
    The calculations were based on the properties of Ag$_2$Se obtained from [$^{[10]}$](https://github.com/KRICT-DATA/SIMD), ensuring realistic and data-driven results.

    ### Optimal Geometries
    Below are two optimal geometries identified for maximizing power output:
    """)

    optimal_geometries = pd.DataFrame({
        "Geometry": ["Compact Design", "Balanced Design"],
        "Length (m)": [0.005, 0.01],
        "Area (m^2)": [0.0005, 0.000275],
        "Resistance (Ω)": [0.00062, 0.00113],
        "Current (A)": [104.24, 57.33],
        "Power (W)": [0.673, 0.37]
    })

    render_html_table(optimal_geometries)

    st.markdown("""
    #### Design Justifications:
    - **Compact Design:** Prioritizes higher power output in a smaller form factor.
    - **Balanced Design:** Provides a balance between power output and manageable current values.

    Both designs demonstrate effective use of material properties to achieve maximum efficiency under realistic constraints.
    """)


# -----------------------------
# TEG unit couple with Ag2Se
# -----------------------------
with st.expander("TEG unit couple with Ag$_2$Se", expanded=False):
    st.markdown("### Building a TEG unit couple by combining the Ag$_2$Se thermoelectric material")
    st.markdown("For choosing a p-type material for buildinig a TEG unit couple with our given material Ag₂Se (n-type) which could results in the best power output from the provided data set reuires a few parameters.")

    st.markdown("1. **Determine the Seebeck Coefficient of the model** (α): The total Seebeck coefficient α$_{tot}$ for a thermoelectric module consisting of p-type and n-type materials is the sum of their individual Seebeck coefficients:")
    st.latex(r"\alpha_{\text{tot}} = \alpha_{p} - \alpha_{n}")
    st.markdown("where α$_{p}$ and α$_{n}$ are the Seebeck coefficients of the p-type and n-type materials, respectively.")

    st.markdown("2. **Determine the Electrical Resistance of the model ($R$)**: The electrical resistance of the thermoelectric legs can be calculated using their electrical conductivity, and length (l) and area of the unit (A):")
    st.latex(r"R_{tot} = R_p + R_n")
    st.markdown("where R$_p$ and R$_n$ are the resistances of p-type and n-type materials, respectively, which can be calculated using their electrical conductivities i.e. $\\sigma_{tot}$ using $\\sigma_p$ and $\\sigma_n$")
    st.latex(r"\frac{1}{\sigma_{tot}} = \frac{1}{\sigma_p} + \frac{1}{\sigma_n}")

    st.markdown("Using the above formula, we can get the total resistance using the below equation, where L is the length and A is the cross-section area of the module, assuming both p-type and n-type has same geometry.")
    st.latex(r"R_{tot} = \frac{L}{A \times \sigma_{tot}}")

    st.markdown("3. **Determinig the Thermal Conductivity ($\\Kappa$)**: The thermal conductance through the thermoelectric materials can be calculated using their thermal conductivity:")
    st.latex(r"\Kappa_{tot} = \Kappa_p + \Kappa_n")

    st.markdown("4. **Temperature difference ($\\Delta$ $T$)**: The temperature difference is set to 100$\\degree$ $C$.")
    st.latex(r"\Delta T = 100 \degree C")

    st.markdown("5. **Voltage Calculation**: The voltage is calculated using the seebeck coefficient and change in temperature: ")
    st.latex(r"V = \alpha \Delta T")

    st.markdown("6. **Current Calculation**: Output current is then calculated using the voltage and the total resistance: ")
    st.latex(r"I = \frac{V}{R_{tot}}")

    st.markdown("7. **Power Output ($P_{out}$)**: The power output for a TEG unit can be calculated using the following formula:")
    st.latex(r"P = \frac{(\alpha \Delta T)^2}{4 \cdot R_{tot}}")

    st.markdown("****")
    st.subheader("Program Overview")
    st.markdown("The temperature difference is set to 100$\\degree C$ i.e. $\\Delta T$ = 100$\\degree C$. Given material is Ag$_2$Se which is an n-type material. From the **database** [$^{[10]}$](https://github.com/KRICT-DATA/SIMD), the best working temperature for Ag$_2$Se is found to between 297\\degree to 399\\degree. The direct average of the parameters such as Seebeck coefficient (α), and electrical conductivity ($\\sigma$) between these two temperature is calculated and used in the above formulae.")
    st.markdown("""A python code was formulated to calculate the best possible p-type material with Ag$_2$Se as it's n-type material in a TEG with the help of all the above mentioned equations. [Python File $^{[11]}$](https://colab.research.google.com/drive/19KxsuC8Po4ldIN2T20bF2U3q8ePTBeXo?usp=sharing)""")

    st.subheader("Resultant maximum power output combination")

    data_ag2se_ptype = {
        'n-type (Formula)': ['Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se'],
        'p-type (Formula)': ['SnS$_{0.91}$Se$_{0.09}$', 'FeNb$_{0.92}$Ti$_{0.08}$Sb', 'Ta$_{0.92}$Ti$_{0.08}$FeSb', 'Ta$_{0.92}$Ti$_{0.08}$FeSb', 'Ta$_{0.88}$Ti$_{0.12}$FeSb'],
        'Voltage (V)': [0.334, 0.250, 0.280, 0.265, 0.255],
        'Current (A)': [68.993834, 91.977306, 81.762653, 83.804931, 86.530423],
        'power output (W)': [23.043940, 22.994327, 22.893543, 22.208307, 22.065258],
    }

    render_html_table(
        pd.DataFrame(data_ag2se_ptype),
        "Table: Combinations of materials with Ag₂Se with maximum power output"
    )

    st.subheader("Conclusion")
    st.markdown("""
    The p-type material which gives the best power output with Ag$_2$Se as n-type material is 
    **SnS$_{0.91}$Se$_{0.09}$**.
    """)


# -----------------------------
# Maximizing Power Output
# -----------------------------
with st.expander("Maximizing Power Output in Thermoelectric Materials", expanded=False):
    st.markdown("""
    ### Maximizing Power Output in Thermoelectric Materials

    To maximize power output, it's crucial to select materials with the following characteristics:

    1. **Seebeck Coefficient ($\\alpha$)**: This is the key factor for generating voltage from temperature differences. A higher Seebeck coefficient will result in greater power generation.
        - **P-type materials**: These have positive Seebeck coefficients (greater than 0), meaning they generate positive voltage when exposed to a temperature gradient.
        - **N-type materials**: These have negative Seebeck coefficients (less than 0), generating negative voltage under the same conditions.

    2. **Electrical Conductivity ($\\sigma$)**: Higher conductivity materials facilitate the movement of charge carriers, which helps in reducing resistive losses. For optimal power output, materials with high electrical conductivity are desired.

    3. **Thermal Conductivity ($\\kappa$)**: A balance between good electrical conductivity and low thermal conductivity is necessary. Materials with lower thermal conductivity help maintain a temperature gradient, which maximizes the power output. 

    4. **Power Factor ($PF$)**: This value reflects the efficiency of the material in converting the Seebeck effect into usable power. Higher power factors are better for thermoelectric applications.

    5. **ZT Value**: The dimensionless figure of merit ($ZT$) is a combination of Seebeck coefficient, electrical conductivity, and thermal conductivity. It determines the overall efficiency of a thermoelectric material.

    #### Power Output Calculation Formula

    The power output for a material pair can be calculated using the formula [10]:
    """)

    st.latex(r"P = \frac{(\alpha \Delta T)^2}{4 \cdot R_{\text{tot}}}")

    st.markdown("""
    Where:
    - **($\\alpha$)** is the difference in Seebeck coefficients between the p-type and n-type materials (in V/K).
    - **($\\Delta T$)** is the temperature difference (in Kelvin).
    - **($R_{\\text{tot}}$)** is the total electrical resistance, which is the sum of the resistances of the p-type and n-type materials.

    #### Material Selection for Maximum Power Output
    To achieve the maximum power output, the ideal combination of materials should have:
    - A large difference in Seebeck coefficients.
    - High electrical conductivity.
    - Low thermal conductivity.
    - High ZT values.

    By combining the right p-type and n-type materials based on these factors, one can maximize the power output for thermoelectric applications.
    """)

    st.markdown("###Program Overview")
    st.markdown("""
    A program was developed based on a comprehensive **database** [$^{[10]}$](https://github.com/KRICT-DATA/SIMD) of thermoelectric materials, which applies a specific approach to identify the optimal material pairs for maximum power output. The program analyzes material properties such as the Seebeck coefficient, electrical conductivity, thermal conductivity, and power factor, and calculates the power output for various material combinations.

    **Combination of Different Materials for n-type and p-type**: 
    The program evaluates all possible combinations of different materials for the n-type and p-type categories, calculating the power output, voltage, and total resistance for each pair. It then ranks the material pairs based on their power output to identify the best-performing combinations.
    """)

    st.markdown("""Python code: [Python File $^{[12]}$](https://colab.research.google.com/drive/14JolgnLB0N8w7kl5sxUPXycHDfPYjGCU#scrollTo=dqLOFJa1T7DU)""")

    optimal_couples = pd.DataFrame({
        "Material p-type": ["FeNb$_{0.92}$Ti$_{0.08}$Sb", "SnS$_{0.91}$Se$_{0.09}$", "FeNb$_{0.92}$Zr$_{0.08}$Sb", "FeNb$_{0.92}$Hf$_{0.08}$Sb"],
        "Material n-type": ["Sr$_{0.21}$Yb$_{0.03}$Co$_{4}$Sb$_{12.12}$", "Sr$_{0.16}$Yb$_{0.03}$Co$_{4}$Sb$_{11.82}$", "Sr$_{0.11}$Ba$_{0.18}$Co$_{4}$Sb$_{12.09}$", "Sr$_{0.21}$Co$_{4}$Sb$_{12.25}$"],
        "Power output (mW)": [60, 57, 54, 52],
        "Voltage (mV)": [23, 32, 22, 24]
    })

    render_html_table(optimal_couples)

    st.markdown("""
    For a pair with maximum output power FeNb$_{0.92}$Ti$_{0.08}$Sb and  Sr$_{0.21}$Yb$_{0.03}$Co$_{4}$Sb$_{12.12}$:
    """)

    st.latex(r"R_{\text{tot}} = 2.17 \ \text{mOhm}")

    st.subheader("FeNb$_{0.92}$Ti$_{0.08}$Sb")
    st.markdown("Temperature dependence of different physical characteristics.")

    display_image_grid(
        [
            'views/python pictures for the temperature deppendence/FeNb0.92Ti0.08Sb_electrical_conductivity.png',
            'views/python pictures for the temperature deppendence/FeNb0.92Ti0.08Sb_seebeck_coefficient.png',
            'views/python pictures for the temperature deppendence/FeNb0.92Ti0.08Sb_thermal_conductivity.png'
        ],
        [
            'views/functions for the comsol/FeNb0.92Ti0.08Sb_conductivity.png',
            'views/functions for the comsol/FeNb0.92Ti0.08Sb_seebeck.png',
            'views/functions for the comsol/FeNb0.92Ti0.08Sb_thermal.png'
        ],
        ratio=1.24
    )

    st.subheader("Sr$_{0.21}$Yb$_{0.03}$Co$_{4}$Sb$_{12.12}$")
    st.markdown("Temperature dependence of different physical characteristics.")

    display_image_grid(
        [
            'views/python pictures for the temperature deppendence/Sr0.21Yb0.03Co4Sb12.12_electrical_conductivity.png',
            'views/python pictures for the temperature deppendence/Sr0.21Yb0.03Co4Sb12.12_seebeck_coefficient.png',
            'views/python pictures for the temperature deppendence/Sr0.21Yb0.03Co4Sb12.12_thermal_conductivity.png'
        ],
        [
            'views/functions for the comsol/Sr0.21Yb0.03Co4Sb12.12_conductivity.png',
            'views/functions for the comsol/Sr0.21Yb0.03Co4Sb12.12_seebeck.png',
            'views/functions for the comsol/Sr0.21Yb0.03Co4Sb12.12_thermal.png'
        ],
        ratio=1.18
    )


# -----------------------------
# Calculating TEG Power and Charging Time
# -----------------------------
with st.expander("Calculating TEG Power and Charging Time for a 5V Output", expanded=False):
    st.markdown("""
    ### Evaluating the Number of TEG Units Needed to Achieve 5V Output
    In this section, we will evaluate the performance of a thermoelectric module (TEG) by calculating the power generated and determining the number of units needed to obtain a voltage of 5V. We will begin by recalling the thermoelectric properties of the material, focusing on its Seebeck coefficient, its thermal conductivity. These parameters are crucial for calculating the voltage and power generated by the module. Next, we will determine how many TEG units are needed to reach the required voltage of 5V, and finally, we will estimate the time needed to charge a phone using this configuration.
    
    ##### Recalling the seebeck coefficient and the thermal conductivity of TEG units
    """)

    data_ag2se_ptype = {
        'n-type (Formula)': ['Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se'],
        'p-type (Formula)': ['SnS$_{0.91}$Se$_{0.09}$', 'FeNb$_{0.92}$Ti$_{0.08}$Sb', 'Ta$_{0.92}$Ti$_{0.08}$FeSb', 'Ta$_{0.92}$Ti$_{0.08}$FeSb', 'Ta$_{0.88}$Ti$_{0.12}$FeSb'],
        'Seebeck coefficient (V/K)': [204.0, 120.0, 150.0, 135.0, 125.0],
        'Thermal conductivity (W/mK)': [2.30, 13.00, 5.99, 6.62, 5.45],
    }

    render_html_table(
        pd.DataFrame(data_ag2se_ptype),
        "Table: Seebeck coefficient and thermal conductivity of the combinations of materials"
    )

    st.markdown("""
    ##### Design of TEG Module for 5V Output
    Based on the table of material combinations with Ag$_2$Se for maximum power output, we have chosen the given differents combinaitions to design a Thermoelectric Generator (TEG) module that generates a 5V output.
    
    To obtain a 5V output with this TEG module, it is necessary to connect multiple modules in series, as the output voltages will sum up. The calculation to determine the number of modules required is as follows:
    
    Let **N** be the **Number of TEG Modules** :
    """)

    st.latex(r"N = \frac{\text{Given voltage}}{\text{Voltage of the TEG}}")

    data_ag2se_ptype = {
        'n-type (Formula)': ['Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se'],
        'p-type (Formula)': ['SnS$_{0.91}$Se$_{0.09}$', 'FeNb$_{0.92}$Ti$_{0.08}$Sb', 'Ta$_{0.92}$Ti$_{0.08}$FeSb', 'Ta$_{0.92}$Ti$_{0.08}$FeSb', 'Ta$_{0.88}$Ti$_{0.12}$FeSb'],
        'Voltage (V)': [0.334, 0.250, 0.280, 0.265, 0.255],
        'Number of TEG_N': [14.970060, 20.000000, 17.857143, 18.867925, 19.607843],
    }

    render_html_table(
        pd.DataFrame(data_ag2se_ptype),
        "Table: Number of TEG for manufacturing the TEG module generating a 5V output voltage"
    )

    st.markdown("Thus, to generate a 5V output, we need to connect **Number of TEG_N** TEG modules in series within the circuit. This configuration will provide the required voltage to charge a mobile phone.")

    st.markdown("""
    ### Estimating Charging Time for a Phone Using a TEG Module
    We assume that we are using as example **a cell phone with a 4200 mAh battery (HUAWEI Nova 7i)** and the charging voltage is **5V**.
    - **Battery capacity** = 4200 mAh = 4,2 Ah
    - **Charging power**= Battery capacity x Charging voltage = 4,2 Ah x 5 V = 21 Wh
    
    Therefore, the phone needs **21 watt-hours of energy** to charge completely.

    We now need to evaluate the charging time **t** process for each TEG unit.
    """)

    st.latex(r"t = \frac{\text{Charging Power}}{\text{Power Output}}")

    st.markdown("##### Summary table")

    data_ag2se_ptype = {
        'n-type (Formula)': ['Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se', 'Ag$_{2}$Se'],
        'p-type (Formula)': ['SnS$_{0.91}$Se$_{0.09}$', 'FeNb$_{0.92}$Ti$_{0.08}$Sb', 'Ta$_{0.92}$Ti$_{0.08}$FeSb', 'Ta$_{0.92}$Ti$_{0.08}$FeSb', 'Ta$_{0.88}$Ti$_{0.12}$FeSb'],
        'Power output (W)': [23.043940, 22.994327, 22.893543, 22.208307, 22.065258],
        'Charging time (hours)': [0.911302, 0.913269, 0.917289, 0.945592, 0.951722],
        'Charging time (min)': [54.678149, 54.796125, 55.037353, 56.735527, 57.103344],
    }

    render_html_table(
        pd.DataFrame(data_ag2se_ptype),
        "Table: Charging time for the cell phone"
    )

    st.markdown("So, we need **t** time for a single TEG module to charge a cell phone with a charging voltage of 5V.")