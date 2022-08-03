#!/usr/bin/python

from pprint import pprint
from sqlite3 import Row
from subprocess import list2cmdline
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from os import listdir, path

c6_database_folder = "/home/acid/Documents/C6_to_send/"
# c6_test_db = path.join(c6_database_folder, 'PM_1ART 1486294_Vouillé_86Z_C6.p')
# c6_xlsx = path.join(c6_database_folder,'PM_1ART 1486294_Vouillé_86Z_C6.xlsx')

def get_only_poteau(pickle_db_poteau):
    list_poteau_c6= [] 
    df = pd.read_pickle(open(pickle_db_poteau,'rb'))
    for el in df:
        # df2= df.filter(like='None', axis=0) 
        # df2 = df[0].dropna()
        df2 = df.filter(like='None', axis=0) 
        df2 = df[0].dropna()
    print(df2)
    for e in df2:
        list_poteau_c6.append(e)   
    return list_poteau_c6

def pandas_exctract(c6):
    df = pd.read_excel(c6, 'Export 1', skiprows=7, header =[0])  
    df = df[['N° appui','Latitude\n(WGS84)','Longitude\n(WGS84)','Adresse de l\'appui (N°, rue ou lieu dit)'] ] 
    # appui = df['N° appui'].dropna() 
    return df[df['N° appui'].notna()] 

def read_all(folder):
    dicdf = {} 
    for file in listdir(folder):
        if file.endswith('.xlsx'):
            dicdf[file.split('_')[2]] = pandas_exctract(path.join(folder, file)) 

    return dicdf

data = read_all('/home/acid/Documents/c6_to_send/')

print(data['ART14'])