from os import listdir, path
import samedi_fiesta
import openpyxl
import postgr
import configlog


width = 330
height = 400
postgr.
class Pt:
    # print("nouvelle appui creér")
    def __init__(self, pt_num):
        self.ptnum = pt_num

    def get_gps(self):
        self.gps_coord = post

        return self.gps_coord


class C6:
    def __init__(self, path_c6Xlsx):
        self.path = path_c6Xlsx
        self.title = path.basename(path_c6Xlsx)

    def get_info(self):
        [nro, sro, pa, art], ptname_row = samedi_fiesta.read_picture_name(self.path)
        self.nro = nro
        self.sro = sro
        self.pa = pa
        self.art = art
        self.ptname_row = ptname_row

    def get_picture(self):
        self.tete_path = samedi_fiesta.add_tete_picture_to_c6(self.ptname_row)
        self.site_path = samedi_fiesta.add_sit_picture_to_c6(self.ptname_row)

    def find_miss(self):
        self.miss_tete = list(self.ptname_row.keys())
        self.miss_site = list(self.ptname_row.keys())
        # print(self.miss_site)
        for pt in self.ptname_row.keys():
            for file in listdir(samedi_fiesta.tete):
                 if file.startswith(self.nro) and pt == file.split('_')[1]:
                    if pt in self.miss_tete:
                        try:
                                self.miss_tete.remove(pt)
                        except :
                            print('deja effacer')
            for file in listdir(samedi_fiesta.site):
                 if file.startswith(self.nro) and pt == file.split('_')[1]:
                    if pt in self.miss_tete:
                        
                        try:
                            self.miss_site.remove(pt)
                        except:
                            print('deja effacer')

    # def fill_picture(self):

    def intial(self):
        self.get_info()
        self.get_picture()
        self.find_miss()

    def actualise_file(self):
        self.position_path_sit = samedi_fiesta.add_sit_picture_to_c6(self.ptname_row)
        self.position_path_tete = samedi_fiesta.add_tete_picture_to_c6(self.ptname_row)

        wb = openpyxl.load_workbook(self.path)
        sheet_photo = wb['Photos']
        for key, value in self.position_path_tete.items():
            thumb = openpyxl.drawing.image.Image(value)
            thumb.height = height
            thumb.width = width
            position = "D" + str(int(key) - 1)
            sheet_photo.add_image(thumb, position)
        for key, value in self.position_path_sit.items():
            thumb = openpyxl.drawing.image.Image(value)
            thumb.height = height
            thumb.width = width
            position = "C" + str(int(key) - 1)
            sheet_photo.add_image(thumb, position)
        # for row in sheet_photo:
        #     remove(sheet_photo, row)
        wb.save(path.join(endroad, self.title))
        wb.close()


def makestat():
    liste = {}
    for c6xlsx in listdir(samedi_fiesta.c6folder):
        try:
            c6 = C6(path.join(samedi_fiesta.c6folder,c6xlsx))
            c6.intial()
            liste[c6.title] = c6
        except:
            print("ereur a la creation de l'instance c6 verifier la fiche : \n{}".format(c6xlsx))
    return liste


# dico_instance_c6 = makestat()
# print(dico_instance_c6)
while 1:
    c6 = input("entre le nom d'une c6 a vérifier")
    test = C6(path.join(samedi_fiesta.c6folder, c6))
    test.intial()