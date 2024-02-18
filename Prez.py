import streamlit as st

# Les titres 
st.title("Analyse des feux de forêts aux USA")
st.sidebar.title("Feux de forêts aux USA")
st.sidebar.header("Un projet en 4 étapes :")

#Les pages
pages=["Compréhension du jeu de données", "Volumétrie du jeu de données",
       "Nettoyage et sélection","Web Scrapping",
       "Statistique","Régionale","Temporelle",
       "Classification","Time Series"]

page = st.sidebar.radio("Cochez la page à afficher", pages)

st.sidebar.subheader("Présentation du jeu de données")
st.sidebar.subheader("Préparation des données")
st.sidebar.subheader("Data Visualisation")
st.sidebar.subheader("Modélisation")


if page == pages[0] :
    st.write("## Compréhension du jeu de données : première exploration")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()
    st.write("https://www.fs.usda.gov/rds/archive/catalog/RDS-2013-0009.6")
    st.divider()

if page == pages[1] :
    st.write("## Volumétrie du jeu de données")
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
    st.write('### La dichotomie des feux')
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
    st.write("## Modèle de classification")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()

if page == pages[8] :
    st.write("## Modélisation temporelle avec Prophet")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()


# Sidebar pour l'équipe
st.sidebar.header("L'équipe")
