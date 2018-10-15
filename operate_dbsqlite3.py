import sqlite3
from contextlib import closing

class accessDBsqlite3():

    def __init__(self,fileName):
        self.__dbname = fileName
        
    def getTable(self, tableName):
        with closing(sqlite3.connect(self.__dbname)) as conn:
            c = conn.cursor()
                
            c.execute(u"select * from %s" % tableName)
            resultList = []
            for x in c.fetchall():
                resultList.append(x)
            return resultList

    def getAllTable(self):
        with closing(sqlite3.connect(self.__dbname)) as conn:
            c = conn.cursor()
                
            c.execute("select * from sqlite_master where type='table'")
            resultList = []
            for x in c.fetchall():
                resultList.append(x)
            return resultList
        
    def createRecode(self, table, recode):
        with closing(sqlite3.connect(self.__dbname)) as conn:
            c = conn.cursor()
                
            sql = u"insert into %s values %s" % (table,recode)
            print(sql)
            c.execute(sql)    
            conn.commit()  
            


