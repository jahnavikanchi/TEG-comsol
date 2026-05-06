import streamlit as st
import base64

st.markdown('''
    <style>
    body {
        color: white;  /* Text color */
        font-family: 'Georgia', sans-serif;  /* Default font */
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


st.markdown("<h1>About Us </h1>", unsafe_allow_html=True)
st.markdown("<h2>Members of Group 1</h2>", unsafe_allow_html=True)

#for making the background image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_jpg_as_page_bg(jpg_file):
    bin_str = get_base64_of_bin_file(jpg_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

background_image_path = 'views/Images/About_us_bg.jpg'
set_jpg_as_page_bg(background_image_path)

# Path for image
def load_image(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()


Violetta = st.columns(2)

with Violetta[0]:
    image_path = "views/Images/Violetta_pfp.jpg"
    image_base64 = load_image(image_path)
    if image_base64:
        st.markdown(f'<img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:100%;">', unsafe_allow_html=True)
with Violetta[1]:
    st.subheader("Project Supervisor a.k.a The Research Maestro")
    st.markdown("<body>Hi! I'm Violetta Korsakova, a 22-year-old from Russia. I recently graduated with a bachelor's degree from Skoltech in Moscow, where I dove deep into electrochemical energy sources for my thesis. Materials science fascinates me because it’s everywhere - from the phone you're holding to future clean energy solutions. I love that I get to explore how new materials can shape the world, especially in ways that support sustainable development. I'm always curious and excited to learn more about how things work - science is my way of exploring the world, and every new discovery keeps me inspired!</body>", unsafe_allow_html=True)

Linda = st.columns(2)

with Linda[0]:
    st.subheader("Project Manager")
    st.write("Linda Maria Carano, 22 year old, Italy. With a Bachelor’s degree in Physics Engineering from Politecnico di Milano. My bachelor thesis was on AFM analysis of the carbonation on the brucite surface. This study focused on understanding the microstructural evolution and reactivity of brucite in response to CO₂, providing insights into its potential for carbon sequestration applications in a circular economy perspective. My passion for science has driven me to pursue a career that contributes positively to society, particularly through sustainable materials research.  Known for my physics-based, analytical approach to problem-solving, I’m committed to addressing global challenges in sustainability and technology through advanced, interdisciplinary training in materials science.")

with Linda[1]:
    image_path = "views/Images/Linda_pfp.jpg"
    image_base64 = load_image(image_path)
    if image_base64:
        st.markdown(f'<img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:100%;">', unsafe_allow_html=True)

Deborah = st.columns(2)

with Deborah[0]:
    image_path = "views/Images/Deborah_pfp.jpg"
    image_base64 = load_image(image_path)
    if image_base64:
        st.markdown(f'<img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:100%;">', unsafe_allow_html=True)

with Deborah[1]:
    st.subheader("Website Manager")
    st.write("I am Deborah SAM, the Website Manager. I come from Ivory Coast and I live in Grenoble to do my engineering study, pursuing  a Master’s program in Advanced Materials at Phelma INP, working towards an engineering degree. I am passionate about science, research, and music, with an extensive background in Materials, Physics and Chemistry provided by PHELMA, along with piano skills at Grade 2. Experienced in collaborating with peers on some academic projects using python, C language, material and electronic projects. Seeking to contribute actively to scientific advancements, I am dedicated to exploring technologies and pushing the boundaries of materials science. I am particularly interested in developing innovative solutions that address real-world challenges. I aspire to be part of pioneering projects that not only expand our understanding of material properties but also drive real impact in industries ranging from electronics to environmental science.")

Jahnavi = st.columns(2)

with Jahnavi[0]:
    st.subheader("The Jack")
    st.write("Hello! I am Kanchi Jahnavi a.k.a ‘The Jack’. I am currently pursuing a master's degree in the field of Functional materials and machine learning. I come from India where I pursued my Bachelor’s degree in the field of materials science and engineering. As an undergrad, I have worked on various projects related to the field of nanoscience, magnetic shielding and battery enhancement. I have delved into machine learning as a personal interest during my studies. The idea of combining the fields of machine learning and materials science has always fascinated me. So, here it goes, my step towards the future for bringing in the fascinating fusion.")
    
with Jahnavi[1]:
    image_path = "views/Images/Jahnavi_pfp.jpg"
    image_base64 = load_image(image_path)
    if image_base64:
        st.markdown(f'<img src="data:image/jpeg;base64,{image_base64}" alt="Image" style="width:100%;">', unsafe_allow_html=True)