import streamlit as st
import base64
import pandas as pd

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


# Section Title
st.markdown('''<h1>Comsol Simulation Results of the Thermoelectric Generator</h1>''', unsafe_allow_html=True)

with st.expander("2. TEG unit couple with Ag$_2$Se"):
  st.subheader("Resultant maximum power output combination")
  st.write("""Based on the findings from the "Optimal Pairings of Two Materials" section, the most suitable p-type material for pairing with Ag$_2$Se  in a thermoelectric generator (TEG) is SnS$_{0.91}$Se$_{0.09}$. This material combination was subsequently analyzed through simulations using the thermoelctric study module (stationary study) of COMSOL Multiphysics® software.""")
  st.write("""First the 3D model of the TEG was built with the following dimensions: 
           """)
  data = {
    "Component": ["Ohmic Contact", "Insulating Contact", "P-type Leg", "N-type Leg"],
    "Dimensions (m)": ["0.005 × 0.006 × 0.0005", "0.017 × 0.006 × 0.001", "0.005 × 0.005 × 0.01", "0.005 × 0.005 × 0.01"]
    }
  df = pd.DataFrame(data)
  html_table = f"""
  <div style="display: flex; justify-content: center;">
    <table style="border-collapse: collapse; border: 2px solid black; text-align: center;">
        {df.to_html(index=False, escape=False)}
    </table>
    </div>
    """
  st.markdown(html_table, unsafe_allow_html=True)
  def load_image(image_file):
        with open(image_file, "rb") as f:
            return base64.b64encode(f.read()).decode()
  image_path1 = "views/Comsol_simulation_images/Scales_.png"
  image_base64 = load_image(image_path1)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:60%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 1: Scales of the model
        </p>
    </div>""", unsafe_allow_html=True)
      
  st.write("""Then, each component is assigned with it's respective material and it's respective properties such as thermal conductivity, seebeck coefficient, etc.""")
  image_path2 = "views/Comsol_simulation_images/Components_Labelled.png"
  image_base64 = load_image(image_path2)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:60%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 2: The assigned materials.
        </p>
    </div>""", unsafe_allow_html=True)
  st.write("""Then the each the conditions to the respective domains or plains were assigned. For this particular simulation the bottom plane is assigned 399K which and the top plane is assigned 299K. Then the p-type ohmic contact is set to be a ground terminal and the n-type ohmic contact is assigned a voltage variable V.""")
  image_path3 = "views/Comsol_simulation_images/Conditions.png"
  image_base64 = load_image(image_path3)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:60%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 3: Figure showcasing the applied conditions to the respective planes.
        </p>
    </div>""", unsafe_allow_html=True)
      
  st.write("""Finally, the simulation is computed. The results included a volumetric temperature gradient, electric field, and electric potential variation""")
  
  image_path4 = "views/Comsol_simulation_images/Final_TempGrad_ag2se.png"
  image_base64 = load_image(image_path4)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:70%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 4: Temperature gradient of TEG.
        </p>
    </div>""", unsafe_allow_html=True)
  st.write("""In figure 4, the temperature difference is 100K. This is the temperature range that we have selected for our material is between 299K-399K which is the same temperature range choosen for theoretical calculation as well.""")
  image_path5 = "views/Comsol_simulation_images/Final_Potential_ag2se.png"
  image_base64 = load_image(image_path5)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:70%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 5: Simulation of the electric potential gradient generated in TEG.
        </p>
    </div>""", unsafe_allow_html=True)
   
  st.write("""From the figure 5, it's found that the the voltage difference that is generated is around 0.033V. From the theoretical calculations of the same TEG module, it was found to be which is about 10e-1 times the theoretically calculated value of voltage. This could be due to the length, which was taken 10e-1 times the original length.\n Power calculated here is 0.225W.""")
    
  image_path6 = "views/Comsol_simulation_images/Final_Field_ag2se.png"
  image_base64 = load_image(image_path6)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:70%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 6: Electric Field generated in TEG.
        </p>
    </div>""", unsafe_allow_html=True)
  
with st.expander("Maximum power ouput for the materials from the database"):
  st.subheader("Maximum power output combination")
  st.write("""At this stage of the project, we transition from analytical calculations to numerical modeling of thermoelectric processes using the finite element method (FEM) in COMSOL Multiphysics. In the preveous part of the study, a simplified version of the problem was solved using analytical equations, allowing us to estimate key parameters of thermoelectric elements such as output power, voltage, and resistance. However, real-world engineering problems are often more complex and require advanced computational methods.

  The main purpose of this stage is to compare the analytical calculations obtained in the previous part with the results of numerical simulations in COMSOL, where the temperature dependences of the material properties obtained in the previous calculations based on the database are used as the main physical characteristics of the material. This approach will allow us to account for more complex physical interactions, such as the distribution of temperature and electric potential within the system, as well as the influence of geometry and material properties. 
  Here we present a couple of materials that have shown maximum power in the theoretical calculations.

  FeNb$_{0.92}$Ti$_{0.08}$Sb and Sr$_{0.21}$Yb$_{0.03}$Co$_{4}$Sb$_{12.12}$ with maximum power output of 60 mW and voltage of 23 mV.
  
  """)
  

  df = pd.DataFrame(data)
  html_table = f"""
  <div style="display: flex; justify-content: center;">
    <table style="border-collapse: collapse; border: 2px solid black; text-align: center;">
        {df.to_html(index=False, escape=False)}
    </table>
    </div>
    """
  st.markdown(html_table, unsafe_allow_html=True)
  def load_image(image_file):
        with open(image_file, "rb") as f:
            return base64.b64encode(f.read()).decode()
  image_path1 = "views/Comsol_simulation_images/V_T1.png"
  image_base64 = load_image(image_path1)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:90%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 1: Volumic Temperaure distribution (K)
        </p>
    </div>""", unsafe_allow_html=True)
      
  st.write("""We then considered the electric potential from which we took the voltage for further calculations of power. V=24.7 mV""")
  image_path2 = "views/Comsol_simulation_images/V_electric_potential.png"
  image_base64 = load_image(image_path2)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:90%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 2: Electric potential (V)
        </p>
    </div>""", unsafe_allow_html=True)
  
      
  st.write("""As a result of calculations of the maximum output power obtained by numerical simulation, we concluded that the results of the analytical calculation (60 mW) are slightly lower than the results obtained by simulation (70 mW). The voltage for this pair obtained by modeling is 24.7 mV, whereas it is 22.9 mV in the analytical calculations.""")
  
  
with st.expander("Number of TEG Units Needed to Achieve 5V Output"):
  st.subheader("15 TEG Units Needed to Achieve 5V Output")
  st.write("""Our objective was to design and manufacture a thermoelectric generator capable of producing the highest possible output power using thermocouples. The working principle was the same as that of a single manufactured thermocouple, but by combining it N times, we could achieve a total power sufficient to charge a Huawei Nova 7i smartphone. To maximize the output power and ensure optimal efficiency, the thermocouples needed to be arranged in series. This configuration allowed the voltages generated by each thermocouple to add up, ultimately reaching the required power level. """)
  

  df = pd.DataFrame(data)
  html_table = f"""
  <div style="display: flex; justify-content: center;">
    <table style="border-collapse: collapse; border: 2px solid black; text-align: center;">
        {df.to_html(index=False, escape=False)}
    </table>
    </div>
    """
  st.markdown(html_table, unsafe_allow_html=True)
  def load_image(image_file):
        with open(image_file, "rb") as f:
            return base64.b64encode(f.read()).decode()
  image_path1 = "views/Comsol_simulation_images/D_T1.png"
  image_base64 = load_image(image_path1)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:60%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 1: Volumic Temperaure distribution (K)
        </p>
    </div>""", unsafe_allow_html=True)
      
  image_path1 = "views/Comsol_simulation_images/D_T2.png"
  image_base64 = load_image(image_path1)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:60%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 1: Volumic Temperaure distribution (K)
        </p>
    </div>""", unsafe_allow_html=True)
      
  st.write("""We then considered the electric fields""")
  image_path2 = "views/Comsol_simulation_images/D_electric_potential.png"
  image_base64 = load_image(image_path2)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:60%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 2: Electric potential (V)
        </p>
    </div>""", unsafe_allow_html=True)
  st.write("""The distribution of the electric field is also considered""")
  image_path3 = "views/Comsol_simulation_images/D_electric_field.png"
  image_base64 = load_image(image_path3)
  if image_base64:
      st.markdown(f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:60%; height:auto;">
        <p style="font-size: 14px; font-weight: bold; margin-top: 5px;">
            Figure 3: Electric field distribution
        </p>
    </div>""", unsafe_allow_html=True)
      