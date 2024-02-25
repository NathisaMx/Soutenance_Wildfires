import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import gdown

with open("stat_méga.pkl", "rb") as fichier_pickle:
    description_feux = pickle.load(fichier_pickle)
    description_Mégafeux = pickle.load(fichier_pickle)
    description_Hors_Méga = pickle.load(fichier_pickle)
    Surf_Total = pickle.load(fichier_pickle)
    Surf_méga= pickle.load(fichier_pickle)
    Part_méga_NB = pickle.load(fichier_pickle)
    Part_méga_surf= pickle.load(fichier_pickle)

with open("Texte/Dispersions.md", "r", encoding="utf-8") as fichier_markdown:
    Com_Dispersions = fichier_markdown.read()

st.set_page_config(page_title="Data Visualisation", page_icon="Fire_logo.png",)
pages=["Data Viz' générale","Data Viz' régionale","Data Viz' temporelle"]

page = st.sidebar.radio("Cliquez sur la partie à afficher", pages)

if page == pages[0]:
    tab1, tab2, tab3 = st.tabs(["Taille des feux","Dichotomie des feux", "Focus sur les Mégafeux"])

    with tab1:
        
        # Centrer le titre
        st.markdown("<h2 style='text-align: center;background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Dispersion statistique comparative des feux selon leur taille (Mégafeux est >= 10 000 Ha)</h2>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([2,6,2,2])
        col1.markdown("<h4 style='text-align: center;'>Ensemble des feux</h4>", unsafe_allow_html=True)
        col2.markdown("<h4 style='text-align: center; background: linear-gradient(to right, navy, orange, red); -webkit-background-clip: text; color: transparent;'>Principales observations</h4>", unsafe_allow_html=True)
        col3.markdown("<h4 style='text-align: center;'>Hors Mégafeux</h4>", unsafe_allow_html=True)
        col4.markdown("<h4 style='text-align: center;'>Mégafeux</h4>", unsafe_allow_html=True)
        col1, col2, col3,col4 = st.columns([2,6,2,2])
        col1.table(description_feux)
        col2.markdown(Com_Dispersions, unsafe_allow_html=True)
        col3.table(description_Hors_Méga)
        col4.table(description_Mégafeux)
        col1, col2, col3 = st.columns([2,8,2])
        col1.write("")
        col2.image("Graphes/Boxplot_Taille.png", width=1000)
        col3.write("")
        


    with tab2:
        st.markdown("<h2 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>La dichotomie des feux</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>Les observations précédentes nous ont conduit à faire une analyse des variables en fonction du nombre de feux et de la surface brûlée</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        st.divider()
        col1.markdown("<h3 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Les feux nombreux, de petite taille,  de cause humaine</h3>", unsafe_allow_html=True)
        col2.markdown("<h3 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Les feux plus rares, de taille importante, de cause naturelle</h3>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,4,1])
        col1.write("")
        col2.image("Graphes/Variable_Classe.png",width=1200)
        col3.write("")
        st.divider()
        col1, col2, col3 = st.columns([1,4,1])
        col1.write("")
        col2.image("Graphes/Variable_Cause.png",width=1200)
        col3.write("")
        st.divider()
        col1, col2, col3 = st.columns([1,4,1])
        col1.write("")
        col2.image("Graphes/Variable_mois.png",width=1200)
        col3.write("")
        st.divider()
        col1, col2, col3 = st.columns([1,4,1])
        col1.write("")
        col2.image("Graphes/Variable_region.png",width=1200)
        col3.write("")
        st.divider()
        col1, col2, col3 = st.columns([1,4,1])
        col1.write("")
        col2.image("Graphes/Variable_vegetation.png",width=1200)
     




    with tab3:
        st.header("Focus sur les mégafeux")

if page == pages[1] :
    st.write("## Régionale")
    st.write('###Titre')
    st.write('blablabla')
    
    st.divider()

if page == pages[2] :
    st.write("## Temporelle")
    st.write('###Titre')
    st.write('blablabla')
    st.image("Variable_année.png", width=1100)
    st.divider()

