import streamlit as st
import leafmap.foliumap as leafmap
import explore

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Selectionne un mode
"""

st.sidebar.title("Zone de Controle")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Streamlit visualisation et traitement des retours")

st.markdown(
    """
    Ce site permet d'echanger des documents d'analyser des photos afin de les classer dans des documents pouvant être rendu a Orange
    Vous pouvez aussi faire de la visualisation de données ainsi que des statistique d'avancement
        """
)

st.header("Instructions")

markdown = """
1. allimente la base de données de tous les document nécéssaire.
2. Rajoute les photos de fin de travaux. 
3. Vérifie les documents créer.
4. Télecharge les documents.
"""
st.markdown(markdown)



# m = leafmap.Map(minimap_control=True)
# m.add_basemap("OpenTopoMap")
# m.to_streamlit(height=500)