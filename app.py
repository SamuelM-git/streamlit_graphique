# La quete sur Streamlit partie 2 - Manipuler des graphiques"

# Les bibliotheques
import streamlit as st
# import matplotlib.pyplot as plt
# import matplotlib as plt
import seaborn as sns
import pandas as pd


# Titre principal de l'application (affiché en haut de la page)
# On utilise le html pour pouvoir centrer le texte
st.markdown("<h1 style='text-align: center; color: red;'>🦁</h1>",
            unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: blue;'>Bienvenue</h1>",
            unsafe_allow_html=True)

st.header("Manipulation de données et création de graphiques", divider=True)

# On telecharge le nom des differnets datasets
liste_data = sns.get_dataset_names()

st.write("Bonjour, nous avons actuellement une liste de ", len(liste_data),
         "dataset(s)")
# On recupere le choix de l'utilisateur
choix = st.selectbox("Lequel veux-tu utiliser ?", liste_data)
# On telecharge le dataset choisi
choix = sns.load_dataset(choix)
# on l'affiche
st.dataframe(choix)

st.write('___')
# On recupere les choix de l'utilisateur pour les 2 colonnes
choix_colonne_x = st.selectbox("Choisissez la colonne X", choix.columns)
# Petit astuce pour ne pas avoir la proposition des 2 colonnes en meme temps
# car ca fait buger le code
list_colonne_2 = choix.columns.copy()
# On va donc extraire dans le 2em selectbox le choix deja fait dans le
# 1ere selectbox
choix_colonne_y = st.selectbox("Choisissez la colonne Y",
                               list_colonne_2.drop(choix_colonne_x))

# On recupere le choix du graphique, mais on cree d'abord une liste avec
# le nom des 3 graphiques
liste_graphique = {'bar_chart', 'line_chart', 'scatter_chart'}
choix_graphique = "scatter_chart"    # le graphique par defaut
choix_graphique = st.selectbox("Quel graphique veux-tu utiliser ?",
                               liste_graphique)

# On applique suivant le choix du graphique
if choix_graphique == "scatter_chart":
    chart_data = pd.DataFrame(choix[[choix_colonne_x, choix_colonne_y]],
                              columns=[choix_colonne_x, choix_colonne_y])
    st.scatter_chart(chart_data, x=choix_colonne_x, y=choix_colonne_y)

elif choix_graphique == "bar_chart":
    chart_data = pd.DataFrame(choix[[choix_colonne_x, choix_colonne_y]],
                              columns=[choix_colonne_x, choix_colonne_y])
    st.bar_chart(chart_data, x=choix_colonne_x, y=choix_colonne_y)

elif choix_graphique == "line_chart":
    chart_data = pd.DataFrame(choix[[choix_colonne_x, choix_colonne_y]],
                              columns=[choix_colonne_x, choix_colonne_y])
    st.line_chart(chart_data, x=choix_colonne_x, y=choix_colonne_y)
st.write('___')

affiche_matrice = st.checkbox("Afficher la matrice de corrélation")
if affiche_matrice:
    # Lorsque la case est cochée, on verifit que l'on a bien 2 colonnes
    # de variables numeriques
    if (choix[choix_colonne_x].dtypes != 'object') and (
       choix[choix_colonne_y].dtypes != 'object'):
        st.header('Ma matrice de corrélation')
        corr_df = choix[[choix_colonne_x, choix_colonne_y]].corr(
            method="pearson")
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_df, annot=True)
        st.pyplot(plt)
        st.balloons()
    else:
        st.snow()
        st.error('Vous devez choisir 2 colonnes ayant des valeurs numériques',
                 icon="🚨")

st.write('___')

st.write("<h7 style='text-align: center; color: green;'>© 2025 Samuel M. All"
         "rights reserved.🦁</h7>", unsafe_allow_html=True)
