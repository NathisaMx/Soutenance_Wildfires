
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# les fichiers dont on a besoin pour l'appli
with open('Pickle/head.pkl', 'rb') as f:
    df_head = pickle.load(f)

with open('Texte/dataset_description.md', 'r',encoding='UTF-8') as f:
    desc = f.read()
  
st.set_page_config(page_title="Présentation du jeu de données", page_icon="Fire_logo.png",layout="wide",)
st.write("## Présentation du projet")
st.divider()
st.image("https://www.fs.usda.gov/sites/default/files/users/user3824/Photos/CWDG/SweetCrk-Milepost2Fire-Marcus-Kauffman.jpg", width=200)
    

st.markdown(desc)
st.write("https://www.fs.usda.gov/rds/archive/catalog/RDS-2013-0009.6")
st.divider()




