import sqlite3
connect = sqlite3.connect('store.db')
cursor = connect.cursor()
cursor.execute("CREATE TABLE SevenEleven \
               (StoreName varchar(20), \
                City varchar(20), \
                Dist varchar(20), \
                No integer primary key, \
                NoName varchar(20),\
                Address text)")
cursor.execute("CREATE TABLE FamilyMart \
               (StoreName varchar(20), \
                City varchar(20), \
                Dist varchar(20), \
                No integer primary key, \
                NoName varchar(20),\
                Address text)")
connect.commit()


