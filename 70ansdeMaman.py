import streamlit as st
from streamlit_option_menu import option_menu
import requests
import folium
from streamlit_folium import st_folium


with st.sidebar :   
    selection = option_menu(
        menu_title=None,
        options = ["Accueil", "Où ?","Organisation"])
 
# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.title("Genviève fête ses 70 ans !")
    st.image("mimi1.jpg")
    
elif selection == "Où ?":
    st.header("Sur l'île d'Oléron")
    point = [45.972916, -1.379777]              # coordo du site
    m = folium.Map(location=point,zoom_start=7)             #carte centrée sur le lieu
    folium.Marker(location=point,popup="L'emplacement idéal pour une fête de folie !").add_to(m)        # marker pour le lieu

    st_folium(m, width=700, height=500) # affichage de la carte
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
    st.image("domino5.jpg")
    st.write('')
    st.header('Pour manger :')
    st.write('Le samedi midi : Comme chacun arrivera à son rythme, nous vous proposons que chacun apporte son pique-nique !')
    st.write("Le samedi soir : On s'occupe de tout 😉")
    st.write("Dimanche midi : Repas en mode 'Auberge espagnole'. Chacun apporte sa p'tite spécialité à partager (ne prévoyez pas trop, l'idée est de rentrer à vide !)")
    st.image("domino6.jpg")



