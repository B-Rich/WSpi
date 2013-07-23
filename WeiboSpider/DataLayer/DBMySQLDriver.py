'''
Created on 2013-6-24

@author: el
'''

import MySQLdb
import string

class DBMySQLDriver:
    def __init__(self, _host, _user, _pass, _port, _dbname):
        self.mHost = _host
        self.mUser = _user
        self.mPass = _pass
        self.mPort = _port
        self.mDBname = _dbname
        
        self.mConn = None
        self.mCursor = None
        
    def CreateDataBase(self):
        try:
            #conn = MySQLdb.connect(host=self.mHost, user=self.mUser, passwd=self.mPass, port=string.atoi(self.mPort), charset="utf-8")
            self.make_connection(withdbname=False)
            self.mCursor.execute("CREATE DATABASE " + self.mDBname)
            self.finish_connection()
        except MySQLdb.Error, e:
            print "MySQL Error in 'CreateDatabase()' %d: %s" % (e.args[0], e.args[1])
            
    def execute(self, clause):
        try:        
            self.make_connection(withdbname=True)
            #clause = clause.encode("utf-8")
            self.mCursor.execute(clause)
            self.finish_connection()
        except MySQLdb.Error, e:
            print("error db execute: %s" % e.args[1])# + ";clause is: " + clause.decode('utf-8', 'ignore').decode('gbk', 'ignore'))
            
    #2 separated courses
    def make_connection(self, withdbname=True):
        if(withdbname == True):
            self.mConn = MySQLdb.connect(host=self.mHost, user=self.mUser, passwd=self.mPass, port=string.atoi(self.mPort), db=self.mDBname, charset="utf8")
        else:
            self.mConn = MySQLdb.connect(host=self.mHost, user=self.mUser, passwd=self.mPass, port=string.atoi(self.mPort), charset="utf8")
        self.mCursor = self.mConn.cursor()
    
    def finish_connection(self):
        self.mConn.commit()
        self.mCursor.close()
        self.mConn.close()
            
    def CreateTable(self, tableName, columns, FKclause=""):
        try:
            self.execute("CREATE TABLE " + tableName + "(" + columns + " " + FKclause + ")")
        except MySQLdb.Error, e:
            print "MySQL Error in 'CreateTable()' %d: %s" % (e.args[0], e.args[1])
            
    def InsertRecord(self, tableName, columns, values):
        try:
            insertStr = "INSERT INTO " + tableName + "(" + columns + ")" + " VALUES" + "(" + values + ")"
            self.execute(insertStr)
        except MySQLdb.Error, e:
            print "MySQL Error in 'InsertRecord()' %d: %s" % (e.args[0], e.args[1])
            
    def UpdateRecord(self, tableName, updateClause, condition):
        try:
            updateStr = "UPDATE " + tableName + " SET " + updateClause + " WHERE " + condition
            self.execute(updateStr)
        except MySQLdb.Error, e:
            print "MySQL Error in 'UpdateRecord()' %d: %s" % (e.args[0], e.args[1])
            
    def TableExists(self, tableName):
        self.make_connection()
        
        count = self.mCursor.execute(
            "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '" + 
            self.mDBname + "' AND TABLE_NAME = '" + tableName + "'")
        
        self.finish_connection()
        
        if count == 0:
            return False
        else:
            return True
    
    def RecExists(self, tableName, fieldKey, fieldValue):
        self.make_connection()
        
        count = self.mCursor.execute(
            "SELECT * FROM " + tableName + " WHERE " + fieldKey + " = " + str(fieldValue))
        
        self.finish_connection()
        
        if count == 0:
            return False
        else:
            return True
    
    def DBExists(self, dbName):
        self.make_connection(withdbname=False)
        
        count = self.mCursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '" + dbName + "'")
        
        self.finish_connection()
        
        if count == 0:
            return False
        else:
            return True
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        