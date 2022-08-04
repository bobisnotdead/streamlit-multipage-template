import sqlite3
from sqlite3 import Error
from os import path, listdir


folder_db = r'/home/acid/Documents/C6_database/'
input_c6 = r'/home/acid/Documents/income_folder/'
python_db = "sqlitedb.py"


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(path.join(folder_db,python_db))
    for file in listdir(folder_db):
        if file.endswith('.py'):
            print(file)