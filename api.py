from .operate_dbsqlite3 import accessDBsqlite3

def getDB(fileName):
    return accessDBsqlite3(fileName)    