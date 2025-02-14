import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar :   
    st.write('Bienvenue root')
    selection = option_menu(
        menu_title=None,
        options = ["Accueil", "Où ?","Organisation"])
 
    # On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.title("Genviève faite ses 70 ans !")
    st.image("Mimi1.jpg")
elif selection == "Où ?":
    st.title("Ils sont pas trop choupinous ???")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("chat1.jpg")
    with col2:
        st.image("chat2.jpg")
    with col3:
        st.image("chat3.jpg")
elif selection == "Organisation" :
    st.title("Organisation :")
    st.write('')
    st.header('Pour dormir :')
    st.write('Les chambres sont composées de 2 ou 4 lits. Nous vous indiquerons votre chambre à votre arrivée !')
    st.write('Des draps peuvent être loués sur place pour ... € ou vous pouvez apporter les votres.')
    st.write('')
    st.header('Pour manger :')
    st.write('Le samedi midi : Comme chacun arrivera à son rythme, nous vous proposons que chacun apporte son pique-nique !')
    st.write("Le samedi soir : On s'occupe de tout 😉")
    st.write("Dimanche midi : Repas en mode 'Auberge espagnole'. Chacun apporte sa p'tite spécialité à partager (ne prévoyez pas trop, l'idée est de rentrer à vide !)")



