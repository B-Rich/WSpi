'''
Created on 2013-6-25

@author: el
'''

import sqlite3

class DBSQLiteDriver:
    
    def __init__(self, _path):
        self.mPath = _path
        self.mConn
        self.mCursor
        
    def open(self):
        self.mConn = sqlite3.connect(self.mPath)
        self.mCursor = self.mConn.cursor()
        
    def close(self, doCommit):
        if(doCommit):
            self.mConn.commit()
            
        self.mCursor.close()
        self.mConn.close()
        
        
    def GetFields(self, valueFieldName, condition):
        self.open()
        
        self.mCursor.execute(
            "SELECT " + valueFieldName + " FROM moz_cookies WHERE " + condition)
        retval = self.mCursor.fetchall()
        
        self.close(False)
        
        return retval
    
    def WipeField(self, value, fieldName, condition):
        self.open()
        
        self.mCursor.execute(
            "UPDATE moz_cookies SET " + fieldName + " = " + value + " WHERE " + condition)
        
        self.close(True)
