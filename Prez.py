import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

# Les titres 
st.title("Analyse des feux de forêts aux USA")
st.sidebar.title("**Feux de forêts aux USA**")
st.sidebar.divider()
st.sidebar.header("Un projet en 4 étapes :")
st.sidebar.subheader("1) Présentation du jeu de données")
st.sidebar.subheader("2) Préparation des données")
st.sidebar.subheader("3) Data Visualisation")
st.sidebar.subheader("4) Modélisation")
st.sidebar.divider()

#Les pages
pages=["1a.Compréhension du jeu de données", "1b.Volumétrie du jeu de données",
       "2a. Nettoyage et sélection","2b.Web Scrapping",
       "3a. Statistique","3b. Régionale","3c. Temporelle",
       "4a. Classification","4b. Time Series"]

page = st.sidebar.radio("                 Cochez la page à afficher", pages)

if page == pages[0] :
    st.write("## Compréhension du jeu de données : première exploration")
    st.divider()
    st.write("https://www.fs.usda.gov/rds/archive/catalog/RDS-2013-0009.6")
    st.divider()
    st.image("https://www.fs.usda.gov/sites/default/files/users/user3824/Photos/CWDG/SweetCrk-Milepost2Fire-Marcus-Kauffman.jpg")

if page == pages[1] :
    st.write("## Préparation des données : complétude des données")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()
if page == pages[2] :
    st.write("## Nettoyage et sélection")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()
if page == pages[3] :
    st.write("## Webscraping")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()
if page == pages[4] :
    st.write("## Statistique")
    st.write('Nous pouvons observer dans le jeu de données, 2 « tendances », avec d’un côté les feux nombreux, de petite taille  avec une cause humaine, et de l’autre les feux plus rares, de taille importante avec une cause naturelle.')
    st.write("Cette dichotomie peut s'observer avec une série de double graphiques sur une même variable :")
    st.write('le premier représente la variable en % du nombre de feux, le second en % de la surface')
    st.divider()
    st.image("Variable_Cause.png")
    st.divider()
    st.image("Variable_Classe.png")
    st.divider()
    st.image("Variable_mois.png")
    st.divider()
    st.image("Variable_année.png")
    st.divider()
    st.image("Variable_region.png")
    st.divider()
    st.image("Variable_vegetation.png")

if page == pages[5] :
    st.write("## Régionale")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()

if page == pages[6] :
    st.write("## Temporelle")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()

if page == pages[7] : 
    st.write('## Modèle de classification')
    st.write('### LogisticRegression')
    st.write('score sur le jeu de test : 0.6471896781847842')
    st.write('score sur le jeu de train: 0.6525264009985726')
    st.write('### RandomForestClassifier')
    st.write('score sur le jeu de test : ')
    st.write('score sur le jeu de train: ')
    st.write('### DecisionTreeClassifier')
    st.write('score sur le jeu de test : 0.5963221118196649')
    st.write('score sur le jeu de train: 0.9997713664254686')
    st.divider()

if page == pages[8] :
    st.write("## Modélisation temporelle avec Prophet")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()
st.sidebar.divider()

st.sidebar.header("L'équipe")


