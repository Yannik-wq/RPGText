import os, sys, sqlite3


a = 0
while a == 0:
    
    if os.path.exists("Classes.db"):                    # Tests if DB Classes already exists
    #print("Datei bereits vorhanden")



        
        connection = sqlite3.connect("Classes.db")                          #Tests if Object Fighter-Class is alraedy part of the db, if not adds Fighter with its attributes, otherwise continues
        cursor = connection.cursor()
        string2 =  "SELECT Name FROM Classes WHERE Nummer = '1'"
        sql = string2
        cursor.execute(sql)
        for dsatz in cursor:
            t = str(dsatz[0])
        if t !='Fighter':
            connection = sqlite3.connect("Classes.db")
            cursor = connection.cursor()
            sql = "INSERT INTO Classes VALUES ('Fighter', '40','40','30','35','30','40','35',"\
                                        "'Simple Strike', 'Overhead Strike','None','None', '1')"
            cursor.execute(sql)
            connection.commit()
    #else:
       # print('Die Klasse '+t+' wurde bereits hinzugefügt') 







        connection = sqlite3.connect("Classes.db")                  # #Tests if Object Rogue-Class is alraedy part of the db, if not adds Fighter with its attributes, otherwise continues
        cursor = connection.cursor()
        string2 =  "SELECT Name FROM Classes WHERE Nummer = '2'"
        sql = string2
        cursor.execute(sql)
        for dsatz in cursor:
           t = str(dsatz[0])
        if t !='Rogue':
            connection = sqlite3.connect("Classes.db")
            cursor = connection.cursor()
            sql = "INSERT INTO Classes VALUES ('Rogue', '35','35','35','45','35','30','35',"\
                                        "'Slash', 'Knife Throw','None','None', '2')"
            cursor.execute(sql)
            connection.commit()
   # else:
       # print('Die Klasse '+t+' wurde bereits hinzugefügt')




    


        connection = sqlite3.connect("Classes.db")                  #Tests if Object Mage-Class is alraedy part of the db, if not adds Fighter with its attributes, otherwise continues
        cursor = connection.cursor()
        string2 =  "SELECT Name FROM Classes WHERE Nummer = '3'"
        sql = string2
        cursor.execute(sql)
        for dsatz in cursor:
            t = str(dsatz[0])
        if t != 'Mage':
            connection = sqlite3.connect("Classes.db")
            cursor = connection.cursor()
            sql = "INSERT INTO Classes VALUES ('Mage', '30','30','50','35','30','30','45',"\
                                "'Magic Bolt', 'Collect Energy','None','None', '3')"
            cursor  .execute(sql)
            connection.commit()
    #else:
        #print('Die Klasse '+t+' wurde bereits hinzugefügt') 
            a = 1
            break
    else:
        connection = sqlite3.connect("Classes.db")              #If ClassesDB doesn't exist yet it is created
        cursor = connection.cursor()


        sql = "CREATE TABLE  Classes(" \
              "Name TEXT, " \
              "Vitality INTEGER," \
              "Strength INTEGER," \
              "Intelligence INTEGER," \
              "Dexterity INTEGER," \
              "Luck INTEGER," \
              "Resilience INTEGER," \
              "ArcaneResistance INTEGER," \
              "AttackMove1 TEXT," \
              "AttackMove2 TEXT," \
              "AttackMove3 TEXT," \
              "AttackMove4 TEXT," \
              "Nummer INTEGER PRIMARY KEY)"

        cursor.execute(sql)

        connection = sqlite3.connect("Classes.db")
        cursor = connection.cursor()





