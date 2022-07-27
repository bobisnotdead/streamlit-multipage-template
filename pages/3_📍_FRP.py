import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("About")
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Fiche Relevé de Parcours")

st.write('section en construction : OCR sur pdf ou image, formulaire de remplissage, export en xlsx')