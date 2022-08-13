from functools import cache
import imp
import streamlit as st
import leafmap.foliumap as leafmap
from os import path
import get_chambre 
import explore_db

@cache
def init():
    nro = explore_db.get_nro()
    return nro


st.set_page_config(layout="wide")
st.sidebar.title("logo")
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)
st.title("Export des c6")


# col1, col2 = st.columns([1,3])
nro_selected = st.selectbox(nro)