import streamlit as st
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
    h2 {
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

st.markdown("<h1>Ag₂Se: A Promising Thermoelectric Material<h1>", unsafe_allow_html=True)
st.markdown("""<body> Silver selenide (Ag₂Se) is a highly efficient thermoelectric material, particularly for applications near room temperature. Its unique combination of electrical and thermal properties, coupled with its phase transition behavior, makes it an ideal candidate for energy conversion and waste heat recovery. Below is an overview of its thermoelectric properties, phase transitions, and mechanisms that drive its performance.
---
</body>""", unsafe_allow_html=True)

    
st.markdown("""
### Crystal Structure

""")
st.markdown("[[MaterialsProject](https://next-gen.materialsproject.org/)")

# Path for image
def load_image(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

image_path = "views/Images/Crystall_sructure.png"
image_base64 = load_image(image_path)
if image_base64:
    st.markdown(f'<img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:100%;">', unsafe_allow_html=True)
             # Add a title under the image
st.markdown("<h3 style='text-align: center;font-size: 16px;'>Ag₂Se crystal structure</h3>", unsafe_allow_html=True)


image_path = "views/Images/Lattice.png"
image_base64 = load_image(image_path)
if image_base64:
    st.markdown(f'<img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:100%;">', unsafe_allow_html=True)
             # Add a title under the image
st.markdown("<h3 style='text-align: center;font-size: 16px;'>Lattice (Conventional)</h3>", unsafe_allow_html=True)

image_path = "views/Images/Symmetry.png"
image_base64 = load_image(image_path)
if image_base64:
    st.markdown(f'<img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:100%;">', unsafe_allow_html=True)
             # Add a title under the image
st.markdown("<h3 style='text-align: center;font-size: 16px;'>Symmetry</h3>", unsafe_allow_html=True)








st.header("Thermoelectric Properties of Ag₂Se")
st.markdown("""
**Ag₂Se**, a promising n-type chalcogenide material, has garnered attention as an ideal candidate for room-temperature thermoelectric applications due to its low thermal conductivity (\( k_{\text{total}} \approx 1 \, \text{W/m·K} \)) and narrow band gap (0.04–0.2 eV). These characteristics contribute to a high \( S^2/\rho \) (figure of merit) at room temperature, making **Ag₂Se** highly suitable for energy conversion and waste-heat recovery technologies[6].
""")


st.header("Phase Transition and Superionic Behavior")
st.markdown("""
Ag₂Se undergoes a significant phase transition from a semiconducting **orthorhombic phase** to a superionic **cubic phase** at approximately 407 K. In the cubic phase, silver ions (Ag⁺) become highly mobile within a rigid selenium lattice. This transition results in metallic conduction and superionic characteristics, which are crucial for enhancing thermoelectric performance. However, the low-temperature orthorhombic phase, while showing promising thermoelectric behavior, is limited by inconsistent \( ZT \) values ranging from 0.3 to 0.96 in the 300–400 K range.[7]
""")

st.header("Achieving High Thermoelectric Performance")
st.markdown("""
Recent advancements have demonstrated a significant improvement in the thermoelectric performance of **Ag₂Se**, achieving \( ZT \) values between 0.9 and 1.0 over the 300–375 K range. This highlights **n-type bulk Ag₂Se** as a competitive material in comparison to state-of-the-art low-temperature thermoelectric materials. The high carrier mobility and low lattice thermal conductivity (0.2–0.1 W/m·K) contribute to its efficiency in converting heat to electricity, even at low temperature differences, such as 80 K.[8]
""")

st.header("Challenges in Achieving Consistent \( ZT \)")
st.markdown("""
One of the main challenges facing the widespread use of **Ag₂Se** in thermoelectric applications is the inconsistency in its figure of merit (\( ZT \)) due to an unoptimized crystal structure and chemical composition. Recent studies have proposed strategies to stabilize the orthorhombic phase and improve carrier mobility by enhancing the material’s defect structure, which can lead to up to a 70% increase in mobility. Additionally, controlling impurities and optimizing the defect structure have been shown to reduce contact resistance, further enhancing the material’s efficiency in thermoelectric devices.[9]
""")
st.latex(r"ZT = \frac{S^2 \sigma T}{k}")


st.markdown("---")






st.markdown("""
**Ag₂Se** is an ideal material for converting heat into electricity, particularly when exposed to heat sources in the **300 K to 400 K** range. Suitable heat sources include:
""")


st.header("1. Industrial Waste Heat")
st.markdown("""
Many industrial processes, such as steel and cement production, release heat in the **200°C to 400°C** range, which can be harnessed by **Ag₂Se** for thermoelectric generation.
""")


st.header("2. Automotive Exhaust")
st.markdown("""
Exhaust gases from vehicles, typically in the **150°C to 500°C** range, provide a reliable source of heat for **Ag₂Se** thermoelectric modules.
""")


st.header("3. Solar Thermal Collectors")
st.markdown("""
These systems capture solar energy, operating within the **100°C to 300°C** range, making them ideal for use with **Ag₂Se** in solar energy applications.
""")

st.header("4. Geothermal Energy")
st.markdown("""
Geothermal heat, typically between **150°C to 300°C**, offers a steady and renewable heat source that **Ag₂Se** can convert into electrical energy.
""")
