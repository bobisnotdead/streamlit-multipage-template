import streamlit as st
import leafmap.foliumap as leafmap
from os import mkdir, path, listdir, rename, chdir
st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://template.streamlitapp.com>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Mesure")
st.write(" possibilité d'uploader les .sor et le fichier txt création du compte rendu en xlsx")
# with st.expander("See source code"):
#     with st.echo():
#         filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
#         m = leafmap.Map(center=[40, -100], zoom=4, tiles="stamentoner")
#         m.add_heatmap(
#             filepath,
#             latitude="latitude",
#             longitude="longitude",
#             value="pop_max",
#             name="Heat map",
#             radius=20,
#         )
# m.to_streamlit(height=700)
with st.form(key="Renseigner les info nécéssaire:", clear_on_submit = False):
    nom = st.text_input("entre le nom de dossier")
    sorfiles = st.file_uploader(label = "Upload sor", type='sor', accept_multiple_files=True)
    Submit = st.form_submit_button(label='Submit')
  
def save_uploadedfile(uploadedfile, destination_path):
     with open(path.join(destination_path, uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))


def make_rename(actual_name,mod):
    actual_name= actual_name.replace

if Submit :
    # Save uploaded file to 'F:/tmp' folder.
    save_folder = path.join('/home/acid/Pictures/Input_folder/mesure/',nom)
    if not path.exists(save_folder):
        mkdir(save_folder)
    for uploadedFile in sorfiles:
        print(uploadedFile.name)
        # ext = uploadedFile.name.split(".")[-1] 
        filep = uploadedFile.name.replace("-","_") 
        filename = '{}-{}_{}'.format(nom, filep.split("_")[10],filep.split("_")[11])
        save_uploadedfile(uploadedFile, save_folder)

    # st.download_button('click ici pour download les mesure traité')
st.write('pour raffracraichir apui  sur f5 gland')