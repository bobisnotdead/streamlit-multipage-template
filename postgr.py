import psycopg2
import sqlalchemy as sa
import explore_db
from os import listdir
import configlog
from sys import warnoptions

if not warnoptions:
    import warnings
    warnings.simplefilter("default")
warnings.filterwarnings('ignore', message='Data Validation extension is not supported and will be removed')
engine = sa.create_engine(configlog.engine)

def read_db_bynro(nro):
    dicodf = explore_db.read_all(configlog.c6initial_folder,nro)
    return dicodf

def get_nro():
    nro = {'nro'}
    for file in listdir(configlog.c6initial_folder):
        nro.add(file.split('_')[0][2:])
        # print(file)
    nro.remove('nro')
    print(nro)
    return nro


def get_table_from_dict(c6dict):
    for key, value in c6dict.items():
        print(key+'\n'+value+'\n')
        # value.to_sql(key, engine)


# df.to_sql('gapminder', engine)

def queryDB(table):
    try:
        connect_str = configlog.connection
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # create a new table with a single column called "name"
        cmd= """CREATE TABLE IF NOT EXISTS {} (name char(40));""".format(table)
        cursor.execute(cmd)

        # run a SELECT statement - no data in there, but we can try it

        conn.commit() # <--- makes sure the change is shown in the database

        cursor.close()

        conn.close()

    except Exception as e:

        print("Uh oh, can't connect. Invalid dbname, user or password?")

        print(e)

nros = get_nro()
for nro in nros:
    
    print(read_db_bynro(nro))
# for el in nros:
#     queryDB(el[2:])