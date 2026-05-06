import streamlit as st
import base64

st.title("Project")
st.subheader('Introduction')

#st.image("views/Images/thermoelectric_intro.jpg", caption="Thermoelectric Energy Illustration", use_column_width=True)


# other Path for image
def load_image(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

image_path = "views/Images/thermoelectric_intro.jpg"
image_base64 = load_image(image_path)
if image_base64:
    st.markdown(f'<img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:100%;">', unsafe_allow_html=True)
             # Add a title under the image
st.markdown("<h3 style='text-align: center;font-size: 16px;'>Thermoelectric Energy Illustration</h3>", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; font-size: 14px;'>
This setup demonstrates thermoelectric generation using a heat source and a cooling mechanism. Candles heat one side of a thermoelectric generator, while a fan-cooled heat sink on the other side creates a temperature difference. This gradient generates electricity, which powers a connected smartphone, showing how heat energy can be converted to electrical energy.
</p>
""", unsafe_allow_html=True)


# Section 1
st.subheader("Thermoelectric Materials: A Path to Sustainable Energy Conversion")
st.write("""
Thermoelectric materials offer a unique solution for converting waste heat into electrical energy directly. This technology relies on the Seebeck effect, which generates power by utilizing temperature differences between a heat source and a cooler area. The efficiency of this process is governed by the Seebeck coefficient (S), which quantifies the voltage produced per unit of temperature difference. Materials with a high Seebeck coefficient are particularly effective in maximizing energy conversion, making them essential for applications like waste heat recovery. By tapping into heat from sources like engines, factories, and human bodies, thermoelectrics provide an efficient means to repurpose otherwise lost energy.

""")

# Section 2
st.subheader("Addressing Energy Efficiency and Environmental Impact")
st.write("""
With a growing need for sustainable energy solutions, thermoelectric technology contributes significantly to energy efficiency and environmental protection. It transforms low-grade waste heat—traditionally challenging to capture—into useful electrical power, offering a promising alternative to reduce dependence on fossil fuels and minimize environmental impact.
""")

# Section 3
st.subheader("Advancements in Flexible Thermoelectric (FTE) Materials")
st.write("""
Recent innovations have led to the development of flexible thermoelectric (FTE) materials, which expand the scope of applications for thermoelectric devices. Unlike rigid, conventional materials, FTEs such as polymers and organic-inorganic hybrids are adaptable for wearable and portable devices. These materials enable energy harvesting from low-temperature sources, like body heat, making them ideal for powering health sensors, personal electronics, and more.
""")

# Section 4
st.subheader("Expanding Applications in Wearables and Portable Devices")
st.write("""
Flexible thermoelectric technology is particularly suited for emerging applications in personal electronics, medical devices, and environmental sensors. These materials facilitate the creation of small, energy-harvesting devices that support self-powered sensors and enable new capabilities in wearables, especially in settings where traditional batteries are less practical.
""")

# Section 5
st.subheader("A Promising Technology for a Greener Future")
st.write("""
Thermoelectric materials, from high-performance rigid systems for industrial recovery to flexible options for wearable devices, present a sustainable approach to power generation, cooling, and self-powered electronics. With continuous advances in materials science and device design, thermoelectrics are well-positioned to support energy efficiency goals and contribute to a cleaner, greener future.
""")