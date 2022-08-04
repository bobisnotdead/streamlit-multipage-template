import streamlit as st
import leafmap.foliumap as leafmap
from os import path
import get_chambre 

def save_uploadedfile(uploadedfile, destination_path):
     with open(path.join(destination_path, uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))
st.set_page_config(layout="wide")

st.sidebar.title("logo")
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)
st.title("Création de la c6")


col1, col2 = st.columns([1,3])

with col1.form(key="Renseigner les info nécéssaire:", clear_on_submit = False):
    selected_sro = col1.selectbox('liste des NRO', get_chambre.sro_list)
    selected_pm = col1.selectbox('liste des SRO', get_chambre.get_pm_by_sro(selected_sro))
    selected_art = col1.selectbox('liste des art', get_chambre.get_picture_by_art(selected_sro, selected_pm))
    seeked_pt = col1.text_input('tape un numéro d\'apuie', value="", max_chars=None, key=None)
    Pictures = col1.file_uploader(label = "Upload pictures", type=["jpeg","png", "JPG"], accept_multiple_files=True)
    c6xlsx = col1.file_uploader(label = "Upload c6", type='xlsx', accept_multiple_files=True)    
    Submit = st.form_submit_button(label='Submit')
    

if Submit :
    # Save uploaded file to 'F:/tmp' folder.
    save_folder = '/home/acid/Pictures/Input_folder/c6/'

    for uploadedFile in Pictures:
        print(uploadedFile.name)
        uploadedFile.name = '{}_{}_{}_{}'.format(selected_sro,selected_pm,selected_art,uploadedFile.name)
        save_uploadedfile(uploadedFile, save_folder)
        st.image(uploadedFile)
    for uploadedFile in c6xlsx:
        print(uploadedFile.name)
        uploadedFile.name = '{}_{}_{}_{}'.format(selected_sro,selected_pm,selected_art,uploadedFile.name)
        save_uploadedfile(uploadedFile, save_folder)
        # st.da (uploadedFile)

        # col2.write(pict.name, save_folder)
    # save_uploadedfile(Pictures, save_folder)
    col2.markdown("**The file is sucessfully Uploaded.**")
    
# 
