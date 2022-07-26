import streamlit as st
import leafmap.foliumap as leafmap
from ... import get_chambre

st.sidebar.title("Selectionne un type de document")
select  = st.sidebar.selectbox('document a traité', ['C6', 'Foa', 'FRP', 'Mesure'] )
if select == 'C6':
    selected_sro = st.selectbox('liste des NRO', get_chambre.sro_list)
    selected_pm = st.selectbox('liste des SRO', get_chambre.get_pm_by_sro(selected_sro))






