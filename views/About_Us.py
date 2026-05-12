import streamlit as st
from pathlib import Path
import base64
import html

st.set_page_config(page_title="About Us", layout="wide")

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

.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 0.2rem;
    color: #12372A;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #526D5B;
    margin-bottom: 3rem;
}

.member-card {
    background: white;
    border-radius: 24px;
    padding: 2rem;
    margin: 0 auto 2.5rem auto;
    max-width: 1250px;

    display: grid;
    grid-template-columns: 340px 1fr;
    gap: 2.5rem;
    align-items: center;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08),
        0 4px 10px rgba(0,0,0,0.04);

    border: 1px solid rgba(0,0,0,0.04);
}

.member-card.reverse {
    grid-template-columns: 1fr 340px;
}

.member-card:hover {
    transform: translateY(-4px);
    box-shadow:
        0 14px 32px rgba(0,0,0,0.10),
        0 6px 14px rgba(0,0,0,0.06);
}

.member-name {
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    color: #12372A !important;
    margin-bottom: 0.4rem;
    line-height: 1.1;
}

.member-role {
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    color: #4F6F52 !important;
    margin-bottom: 1.2rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.member-text {
    font-size: 1rem;
    line-height: 1.8;
    text-align: justify;
    color: #374151;
}

.profile-container {
    display: flex;
    justify-content: center;
    align-items: center;
}

.profile-img {
    width: 320px;
    height: 320px;
    object-fit: cover;
    border-radius: 20px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.12);
}

@media screen and (max-width: 900px) {
    .member-card,
    .member-card.reverse {
        grid-template-columns: 1fr;
        text-align: center;
    }

    .member-text {
        text-align: justify;
    }

    .profile-img {
        width: 260px;
        height: 260px;
    }
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="main-title">About Us</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Meet the Team!</div>', unsafe_allow_html=True)


# -----------------------------
# Team Data
# -----------------------------
members = [
    {
        "name": "Violetta Korsakova",
        "role": "Project Supervisor a.k.a The Research Maestro",
        "image": "views/Images/Violetta_pfp.jpg",
        "bio": "Hi! I'm Violetta Korsakova, a 22-year-old from Russia. I recently graduated with a bachelor's degree from Skoltech in Moscow, where I dove deep into electrochemical energy sources for my thesis. Materials science fascinates me because it’s everywhere - from the phone you're holding to future clean energy solutions. I love that I get to explore how new materials can shape the world, especially in ways that support sustainable development. I'm always curious and excited to learn more about how things work - science is my way of exploring the world, and every new discovery keeps me inspired!"
    },
    {
        "name": "Linda Maria Carano",
        "role": "Project Manager",
        "image": "views/Images/Linda_pfp.jpg",
        "bio": "Linda Maria Carano, 22 year old, Italy. With a Bachelor’s degree in Physics Engineering from Politecnico di Milano. My bachelor thesis was on AFM analysis of the carbonation on the brucite surface. This study focused on understanding the microstructural evolution and reactivity of brucite in response to CO₂, providing insights into its potential for carbon sequestration applications in a circular economy perspective. My passion for science has driven me to pursue a career that contributes positively to society, particularly through sustainable materials research. Known for my physics-based, analytical approach to problem-solving, I’m committed to addressing global challenges in sustainability and technology through advanced, interdisciplinary training in materials science."
    },
    {
        "name": "Deborah SAM",
        "role": "Website Manager",
        "image": "views/Images/Deborah_pfp.jpg",
        "bio": "I am Deborah SAM, the Website Manager. I come from Ivory Coast and I live in Grenoble to do my engineering study, pursuing a Master’s program in Advanced Materials at Phelma INP, working towards an engineering degree. I am passionate about science, research, and music, with an extensive background in Materials, Physics and Chemistry provided by PHELMA, along with piano skills at Grade 2. Experienced in collaborating with peers on some academic projects using python, C language, material and electronic projects. Seeking to contribute actively to scientific advancements, I am dedicated to exploring technologies and pushing the boundaries of materials science. I am particularly interested in developing innovative solutions that address real-world challenges. I aspire to be part of pioneering projects that not only expand our understanding of material properties but also drive real impact in industries ranging from electronics to environmental science."
    },
    {
        "name": "Kanchi Jahnavi",
        "role": "The Jack",
        "image": "views/Images/Jahnavi_pfp.jpg",
        "bio": "Hello! I am Kanchi Jahnavi a.k.a ‘The Jack’. I am currently pursuing a master's degree in the field of Functional materials and machine learning. I come from India where I pursued my Bachelor’s degree in the field of materials science and engineering. As an undergrad, I have worked on various projects related to the field of nanoscience, magnetic shielding and battery enhancement. I have delved into machine learning as a personal interest during my studies. The idea of combining the fields of machine learning and materials science has always fascinated me. So, here it goes, my step towards the future for bringing in the fascinating fusion."
    }
]


# -----------------------------
# Render Members
# -----------------------------
for i, member in enumerate(members):
    image_base64 = img_to_base64(member["image"])

    safe_name = html.escape(member["name"])
    safe_role = html.escape(member["role"])
    safe_bio = html.escape(member["bio"])

    if image_base64:
        image_html = f'<div class="profile-container"><img class="profile-img" src="data:image/jpeg;base64,{image_base64}"></div>'
    else:
        image_html = '<div class="profile-container"><p>Image not found</p></div>'

    text_html = f'<div class="member-info"><div class="member-name">{safe_name}</div><div class="member-role">{safe_role}</div><div class="member-text">{safe_bio}</div></div>'

    if i % 2 == 0:
        card_class = "member-card"
        card_content = image_html + text_html
    else:
        card_class = "member-card reverse"
        card_content = text_html + image_html

    st.markdown(
        f'<div class="{card_class}">{card_content}</div>',
        unsafe_allow_html=True
    )