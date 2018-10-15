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

