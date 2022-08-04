import psycopg2
import sqlalchemy as sa
import explore_db

engine = sa.create_engine('postgresql://acid: q@localhost:5432/darkpad')
nro = explore_db.get_nro()
dicodf = explore_db.read_all('/home/acid/Documents/c6_to_send/','BVR')

def get_table_from_dict(c6dict):
    for key, value in c6dict.items():
        value.to_sql(key, engine)


get_table_from_dict(dicodf)

# df.to_sql('gapminder', engine)

def oldway():
    try:
        connect_str = "dbname='darkpad' user='acid' host='localhost' " + "password=' q'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # create a new table with a single column called "name"
        cursor.execute("""CREATE TABLE sro (name char(40));""")

        # run a SELECT statement - no data in there, but we can try it

        cursor.execute("""SELECT * from nro""")

        conn.commit() # <--- makes sure the change is shown in the database

        rows = cursor.fetchall()

        print(rows)

        cursor.close()

        conn.close()

    except Exception as e:

        print("Uh oh, can't connect. Invalid dbname, user or password?")

        print(e)
