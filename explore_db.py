#!/usr/bin/python


import pandas as pd
import matplotlib.pyplot as plt
import pickle
from os import listdir, path
import sqlite3

c6_database_folder = "/home/acid/Documents/c6_to_send"
sqlite_db ='/home/acid/Documents/sqlitedb/sqlit_db'
conn = sqlite3.connect(sqlite_db) 
c = conn.cursor()
# c6_database_folder = "/home/acid/Documents"

# c6_test_db = path.join(c6_database_folder, 'PM_1ART 1486294_Vouillé_86Z_C6.p')
# c6_xlsx = path.join(c6_database_folder,'PM_1ART 1486294_Vouillé_86Z_C6.xlsx')
nro = {'nro'}

def get_nro():
    for file in listdir(c6_database_folder):
        nro.add(file.split('_')[0])
        # print(file)
    return nro


def pandas_exctract(c6):
    df = pd.read_excel(c6, 'Export 1', skiprows=7, header =[0])  
    df = df[['N° appui','Latitude\n(WGS84)','Longitude\n(WGS84)','Adresse de l\'appui (N°, rue ou lieu dit)'] ] 
    # appui = df['N° appui'].dropna() 
    return df[df['N° appui'].notna()] 

def read_all(folder, nro):
    dicdf = {} 
    for file in listdir(folder):
        if file.endswith('.xlsx') and file.startswith(nro):
            df = pandas_exctract(path.join(folder, file)) 
            dicdf[file.split('_')[2]] = df 
            # cmd = 'CREATE TABLE IF NOT EXISTS BVR (N° appui,Latitude\n(WGS84),Longitude\n(WGS84),Adresse de l\'appui (N°, rue ou lieu dit))' 
            # c.execute(cmd)  
            # conn.commit()
            # df.to_sql(nro, conn, if_exists='replace', index = False)
    return dicdf


data = read_all('/home/acid/Documents/c6_to_send/','BVR')

print(data)