import streamlit as st
from streamlit_option_menu import option_menu
import requests
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Anniversaire de Mimi", layout="wide")

# Appliquer un fond vert olive + texte beige
st.markdown(
    """
    <style>
        /* Fond principal */
        .stApp {
            background-color: #608270;  /* Mode Olive */
        }

        /* Texte principal en beige et centré */
        h1, h2, h3, h4, h5, h6, p, div, span, label {
            color: #F5F5DC !important;  /* Beige */
            text-align: center !important;  /* Centrer le texte */
        }

        /* Modifier la couleur des inputs et boutons */
        .stTextInput > label, .stButton > button {
            color: #F5F5DC !important;  /* Beige */
        }

        /* Centrer le titre */
        .title {
            text-align: center
        }

    </style>
    """,
    unsafe_allow_html=True
)


with st.sidebar :   
    selection = option_menu(
        menu_title=None,
        options = ["Accueil", "Où ?","Organisation"])
 
# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.title("Geneviève fête ses 70 ans !")
    col1, col2, col3 = st.columns([1, 2, 1])  # La colonne du milieu est plus grande
    with col2:
        st.image("mimi1.jpg",width=700)
    st.header('Réservez dès maintenant votre Weekend du 6 et 7 avril 2025 !')
    
elif selection == "Où ?":
    st.header("Sur l'île d'Oléron")
    st.write("Au cœur du village de Domino, dans la commune de Saint-Georges-d’Oléron, à seulement 700m de la plage !")
    point = [45.972916, -1.379777]              # coordo du site
    m = folium.Map(location=point,zoom_start=7)             #carte centrée sur le lieu
    folium.Marker(location=point,popup="L'emplacement idéal pour une fête de folie !").add_to(m)        # marker pour le lieu
    col1, col2, col3 = st.columns([1, 2, 1])  # La colonne du milieu est plus grande
    with col2:
        st_folium(m, width=700, height=500) # affichage de la carte

    st.write("111-25 Rue Aristide Briand")
    st.write("17190 Saint-Georges-d'Oléron")
    st.write("")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("domino1.jpg")
    with col5:
        st.image("domino2.jpg")
    with col6:
        st.image("domino3.jpg")

elif selection == "Organisation" :
    st.title("Organisation :")
    st.write('')
    st.header('Pour dormir :')
    st.write('Les chambres sont composées de 2 ou 4 lits. Nous vous indiquerons votre chambre à votre arrivée !')
    st.write('Des draps peuvent être loués sur place pour ... € ou vous pouvez apporter les votres.')
    col1, col2, col3 = st.columns([1, 1, 1])  # La colonne du milieu est plus grande
    with col2:
        st.image("domino5.jpg",width=400)
    st.write('')
    st.header('Pour manger :')
    st.write('Le samedi midi : Comme chacun arrivera à son rythme, nous vous proposons que chacun apporte son pique-nique !')
    st.write("Le samedi soir : On s'occupe de tout 😉")
    st.write("Dimanche midi : Repas en mode 'Auberge espagnole'. Chacun apporte sa p'tite spécialité à partager (ne prévoyez pas trop, l'idée est de rentrer à vide !)")
    col1, col2, col3 = st.columns([1, 1, 1])  # La colonne du milieu est plus grande
    with col2:
        st.image("domino6.jpg",width=400)



