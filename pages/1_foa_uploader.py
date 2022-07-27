# import libraries
from distutils.command.upload import upload
from os import path
import streamlit as st
import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np


col1, col2, col3 = st.columns([1,2,1])
img_file_buffer = col1.camera_input("Prise des photos terrain")


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
col2.title('Transfert de dossier')
# clicked = col1.button('Selectionne un dossier')
# if clicked:
#     dirname = st.text_input('Selected folder:', filedialog.askdirectory(master=root))

# c6upload = st.file_uploader('Mettre la c6 a traiter', type="xlsx", accept_multiple_files=True, key=None, help=None, on_change=None )
with col2.form(key="Renseigner les info nécéssaire:", clear_on_submit = False):
    Room_number  = col2.text_input('numéros de la chambre')
    commande = col2.text_input("N° de commande : ")
    Adresse = col2.text_input("Adresse: ")
    Type = col2.selectbox('type  de chambre',['OHN','K1C', 'K2C', 'L1T', 'L2T', 'L3T']  )	
    Pictures = col2.file_uploader(label = "Upload picture", type=["jpeg","png", "JPG"], accept_multiple_files=True)
    Submit = st.form_submit_button(label='Submit')
    

if Submit :
    # Save uploaded file to 'F:/tmp' folder.
    save_folder = '/home/acid/Pictures/Input_folder/foa/'
    print(Adresse)
    print(Pictures)
    i=0
    for uploadedFile in Pictures:
        print(uploadedFile.name)
        ext = uploadedFile.name.split(".")[-1] 
        uploadedFile.name ='{}_{}_{}_{}_{}.{}'.format(Room_number,commande,Adresse,Type,i,ext)
        save_uploadedfile(uploadedFile, save_folder)
        i+=1
        col3.image(uploadedFile)

        # col2.write(pict.name, save_folder)
    # save_uploadedfile(Pictures, save_folder)
    col2.markdown("**The file is sucessfully Uploaded.**")
# with col3:

#     if img_file_buffer is not None:
#     # To read image file buffer with OpenCV:
#         bytes_data = img_file_buffer.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

#     # Check the type of cv2_img:
#     # Should output: <class 'numpy.ndarray'>
#     st.write(type(cv2_img))

#     # Check the shape of cv2_img:
#     # Should output shape: (height, width, channels)
#     st.write(cv2_img.shape)


