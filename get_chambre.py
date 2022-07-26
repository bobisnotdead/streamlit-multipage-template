from os import walk, path, listdir

retour = '/home/acid/martillac/retour_travaux/'
sro_list = listdir(retour)


def get_pm_by_sro(selected_sro):
    list_pm = listdir(path.join(retour, selected_sro))
    return list_pm


def get_picture_by_art(selected_sro, selected_pm):
    art_list = [] 
    pm_folder = path.join(retour,selected_sro, selected_pm) 
    for folder in listdir(pm_folder):
        art = path.join(pm_folder,folder) 
        if 'PHOTOS' in listdir(art):
            art_list.append(folder)
    return art_list

get_picture_by_art()


