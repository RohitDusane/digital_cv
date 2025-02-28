from pathlib import Path
import streamlit as st
from PIL import Image
import os

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "Profile picture.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Biostatistician Digital CV | Jane Doe"
PAGE_ICON = ":wave:"
NAME = "Jane Doe"
DESCRIPTION = """
Biostatistician specializing in statistical modeling, data analysis, and epidemiology. Helping researchers and institutions derive insights from complex health data.
"""
EMAIL = "janedoe@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/janedoe",
    "GitHub": "https://github.com/janedoe",
    "ResearchGate": "https://www.researchgate.net/profile/Jane_Doe",
}
PROJECTS = {
    "🏆 Clinical Trial Analysis - Survival analysis and Kaplan-Meier curves": "https://www.example.com/project1",
    "🏆 Epidemiological Study - Analyzing COVID-19 incidence and prevalence": "https://www.example.com/project2",
    "🏆 Bioinformatics Tool - Gene expression analysis using R": "https://www.example.com/project3",
}

# --- Set Page Configuration ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- Load Custom CSS ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Load Resume and Profile Pic ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
    ✔️ 5+ years of experience in biostatistics and epidemiological analysis  
    ✔️ Expertise in survival analysis, hypothesis testing, and statistical modeling  
    ✔️ Proficient in R, SAS, Python (SciPy, NumPy, Pandas), SPSS, and STATA  
    ✔️ Familiar with clinical trial design, longitudinal studies, and epidemiological surveys  
    ✔️ Strong understanding of biostatistical methodologies including linear/logistic regression, mixed-effects models, and meta-analysis  
    ✔️ Excellent communication skills for presenting complex statistical results to non-technical stakeholders
    """
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
    👩‍💻 Programming: R (ggplot2, dplyr, caret), Python (SciPy, Pandas), SAS, STATA  
    📊 Data Visualization: R (ggplot2, Shiny), Python (Matplotlib, Seaborn), Tableau  
    📚 Statistical Modeling: Cox Proportional Hazards, Logistic Regression, ANOVA, Meta-Analysis  
    🗄️ Databases: MySQL, PostgreSQL, MongoDB
    """
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Biostatistician | Global Health Research Institute**")
st.write("02/2020 - Present")
st.write(
    """
► Led statistical analysis for epidemiological studies focused on chronic disease prevalence using R and SAS  
► Developed statistical models (e.g., survival analysis, Cox models) for clinical trial data to identify key risk factors  
► Collaborated with healthcare professionals to design and analyze longitudinal studies on cancer outcomes  
► Presented findings to clinical research teams and contributed to peer-reviewed publications  
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Biostatistician | National Institutes of Health (NIH)**")
st.write("01/2018 - 02/2020")
st.write(
    """
► Conducted statistical analysis on data from randomized controlled trials, using SAS and R for hypothesis testing  
► Applied mixed-effects models to longitudinal health data to analyze the impact of intervention strategies  
► Collaborated with research teams to design surveys and analyze epidemiological data for public health reports  
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Junior Biostatistician | Health Data Analytics Ltd**")
st.write("05/2015 - 01/2018")
st.write(
    """
► Assisted in the design and analysis of clinical studies, focusing on health outcomes and quality of life measures  
► Applied statistical methods (t-tests, ANOVA) to compare treatment efficacy across clinical trial groups  
► Supported bioinformatics analysis and gene expression data processing using R  
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
