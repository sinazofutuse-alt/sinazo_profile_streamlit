# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 20:48:19 2026

@author: FutuseS
"""

import streamlit as st
import pandas as pd
import numpy as np

# 
# PAGE CONFIG
# 
st.set_page_config(
    page_title="Sinazo Futuse | Research & Agribusiness Profile",
    layout="wide"
)

# 
# Information
# 
name = "Sinazo Futuse"
field = "Microbiology & Biotechnology"
institution = "University of Johannesburg"
email = "sinazofutuse@gmail.com"

# 
# TITLE
# 
st.title("👩🏽‍🔬 Sinazo Futuse")
st.subheader("Researcher | MSc Biotechnology | Agribusiness")

# 
# SIDEBAR
# 
menu = st.sidebar.radio(
    "Navigation",
    [
        "Profile Overview",
        "Education & Skills",
        "Research & Publications",
        "MSc Research Project (UJ)",
        "Current Work (ARC & UJ)",
        "Agribusiness: Citrus Farming",
        "STEM Data Explorer",
        "Contact"
    ]
)

# 
# PROFILE OVERVIEW
# 
if menu == "Profile Overview":
    st.header("Profile Overview")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "https://cdn.pixabay.com/photo/2017/01/20/00/30/microscope-1996280_1280.jpg",
            caption="Scientific Research"
        )

    with col2:
        st.write(f"**Name:** {name}")
        st.write(f"**Field:** {field}")
        st.write(f"**Institution:** {institution}")
        st.write("""
        I am a motivated microbiology researcher with strong laboratory,
        molecular biology, and data analysis skills. My work focuses on
        antimicrobial resistance, food safety, and applied agricultural
        biotechnology.
        """)

# ===============================
# EDUCATION & SKILLS
# ===============================
elif menu == "Education & Skills":
    st.header("Education")

    st.markdown("""
    **BSc in Biochemistry & Microbiology**  
    University of Fort Hare (2022)

    **BSc Honours in Microbiology**  
    University of Fort Hare (2023)

    **MSc in Biotechnology** *(In progress)*  
    University of Johannesburg
    """)

    st.header("Technical Skills")
    skills = [
        "PCR, gel electrophoresis and molecular techniques",
        "Fungal isolation, culturing and identification",
        "Antibiotic susceptibility testing",
        "LC-MS/MS mycotoxin analysis (theoretical & applied)",
        "Data analysis and scientific reporting",
        "Python for data analysis and visualisation"
    ]
    st.write(skills)

# ===============================
# RESEARCH & PUBLICATIONS
# ===============================
elif menu == "Research & Publications":
    st.header("Research Background")

    st.subheader("Honours Research Project")
    st.markdown("""
    **Assessment of antibiogram profile of *Escherichia coli* isolated from hospital effluent**

    - Isolation and confirmation of *E. coli* using PCR  
    - Antimicrobial susceptibility testing  
    - Detection of resistance genes  
    - Public health implications of antibiotic resistance  
    """)

    st.subheader("Publications (Optional Upload)")
    uploaded_file = st.file_uploader("Upload publications CSV", type="csv")

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

# ===============================
# MSC PROJECT
# ===============================
elif menu == "MSc Research Project (UJ)":
    st.header("MSc Research Project – University of Johannesburg")

    st.subheader("Project Title")
    st.markdown("""
    **Prevalence of Fungi and Mycotoxins along the Dairy Cattle Farm Value Chain
    in Selected Provinces of South Africa**
    """)

    st.subheader("Supervision")
    st.write("""
    - **Supervisor:** Prof. P. B. Njobeh  
    - **Co-Supervisor:** Dr J. Z. Phoku (Agricultural Research Council)
    """)

    st.subheader("Aim")
    st.write("""
    To assess the prevalence and levels of fungal contamination and mycotoxin
    occurrence along dairy farms in selected provinces of South Africa.
    """)

    st.subheader("Objectives")
    st.markdown("""
    1. Isolation and identification of fungal species from dairy feeds  
    2. Detection and quantification of mycotoxins in feed, milk and urine using LC-MS/MS  
    3. Evaluation of cytotoxicity potential using MTT assay  
    """)

    st.subheader("Methodology Overview")
    st.markdown("""
    - Sampling from commercial and subsistence dairy farms  
    - Morphological and molecular fungal identification (ITS PCR)  
    - Multi-mycotoxin analysis using LC-MS/MS  
    - Statistical analysis using ANOVA and correlation tests  
    """)

# ===============================
# CURRENT WORK
# ===============================
elif menu == "Current Work (ARC & UJ)":
    st.header("Current Professional Work")

    st.subheader("Agricultural Research Council (ARC)")
    st.write("""
    - Laboratory-based agricultural and food safety research  
    - Exposure to mycotoxin and fungal analysis  
    - Research data handling and reporting
    """)

    st.subheader("University of Johannesburg (UJ)")
    st.write("""
    - MSc research activities in biotechnology  
    - Laboratory experiments and academic research  
    - Collaboration with supervisors and research teams
    """)

# ===============================
# AGRIBUSINESS
# ===============================
elif menu == "Agribusiness: Citrus Farming":
    st.header("Citrus Farming Agribusiness")

    st.subheader("Jerusalem Farm")
    st.write("""
    - Involvement in citrus production and farm operations  
    - Integration of scientific principles into agriculture  
    - Focus on sustainability and food security
    """)

    farm_data = pd.DataFrame({
        "Activity": ["Planting", "Irrigation", "Harvesting", "Packaging"],
        "Status": ["Completed", "Ongoing", "Seasonal", "Ongoing"]
    })

    st.dataframe(farm_data)

# ===============================
# STEM DATA
# ===============================
elif menu == "STEM Data Explorer":
    st.header("STEM Data Explorer")

    physics_data = pd.DataFrame({
        "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Analysis"],
        "Energy (MeV)": [4.2, 1.5, 2.9]
    })

    astronomy_data = pd.DataFrame({
        "Object": ["Mars", "Venus", "Jupiter"],
        "Brightness": [-2.0, -4.6, -1.8]
    })

    choice = st.selectbox("Select dataset", ["Physics", "Astronomy"])

    if choice == "Physics":
        st.dataframe(physics_data)
        st.bar_chart(physics_data.set_index("Experiment"))

    else:
        st.dataframe(astronomy_data)
        st.bar_chart(astronomy_data.set_index("Object"))

# ===============================
# CONTACT
# ===============================
elif menu == "Contact":
    st.header("Contact Information")
    st.write(f"📧 Email: {sinazofutuse@gmail.com}")
    st.write("📍 South Africa")
