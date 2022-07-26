from os import path
from xml.etree.ElementTree import PI
# import libraries
import streamlit as st
import tkinter as tk
from tkinter import filedialog


def save_uploadedfile(uploadedfile, destination_path):
     with open(path.join(destination_path, uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))
# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button
st.title('Transfert de dossier')
col1, col2, col3 = st.columns([1,3,1])
# clicked = col1.button('Selectionne un dossier')
# if clicked:
#     dirname = st.text_input('Selected folder:', filedialog.askdirectory(master=root))

# c6upload = st.file_uploader('Mettre la c6 a traiter', type="xlsx", accept_multiple_files=True, key=None, help=None, on_change=None )

col3.markdown("**Please fill the below form :**")
with st.form(key="Renseigner les info nécéssaire:", clear_on_submit = False):
    Room_number  = st.text_input('numéros de la chambre')
    commande = st.text_input("N° de commande : ")
    Adresse = st.text_input("Adresse: ")
    Type = st.selectbox('type  de chambre',['OHN','K1C', 'K2C', 'L1T', 'L2T', 'L3T']  )	
    Pictures = st.file_uploader(label = "Upload picture", type=["jpeg","png", "JPG"], accept_multiple_files=True)
    Submit = st.form_submit_button(label='Submit')
    

if Submit :
    # Save uploaded file to 'F:/tmp' folder.
    save_folder = '/home/acid/Pictures/Input_folder/'
    print(Adresse)
    print(Pictures)
    for uploadedFile in Pictures:
        print(uploadedFile.name)
        save_uploadedfile(uploadedFile, save_folder)


        # st.write(pict.name, save_folder)
    # save_uploadedfile(Pictures, save_folder)
    st.markdown("**The file is sucessfully Uploaded.**")
