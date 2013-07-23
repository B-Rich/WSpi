'''
Created on 2013-6-25

@author: el

'''
from xml.etree import ElementTree
from Structures import ws_st_threadconf
import re
import os

class ParametersPlatform:
    
    def __init__(self, _path):
        self.mBasePath = _path 
        self.mParaFilePath = GetParaFilePath(_path)
        self.mRoot = ElementTree.parse(self.mParaFilePath)
        
    def GetAllTheradsNames(self):
        
        threadNodes = self.mRoot.getiterator("thread")
        retval = []
        for node in threadNodes:
            retval.append(node.attrib['iden'])
            
        return retval
        
    def getThreadNode(self, iden):
        
        threadNodes = self.mRoot.getiterator("thread")
        for node in threadNodes:
            if(node.attrib['iden'] == iden):
                return node
        
        return None
    
    def GetTaskParameters(self, iden):
        node = self.getThreadNode(iden)
        if(node != None):
            taskParas = ws_st_threadconf.ws_st_threadconf()
            taskParas.iden = iden
            taskParas.user = node.attrib['user']
            taskParas.password = node.attrib['password']
            taskParas.callbackAddr = node.attrib['callbackAddr']
            taskParas.appKey = node.attrib['appKey']
            taskParas.appSecret = node.attrib['appSecret']
            taskParas.queryClause = node.attrib['queryClause']
            taskParas.carryover = node.attrib['carryover']
            taskParas.dbhost = node.attrib["dbhost"]
            taskParas.dbname = node.attrib["dbname"]
            taskParas.dbuser = node.attrib["dbuser"]
            taskParas.dbpass = node.attrib["dbpass"]
            taskParas.dbport = node.attrib["dbport"]
            taskParas.requestPerHour = node.attrib["requestPerHour"]
            return taskParas
        else:
            return None
        
def FuncParaParser(queryString):
    rex = re.compile(r"\w+")
    mts = rex.findall(queryString)
    return mts

def GetParaFilePath(basepath):
    return os.path.join(basepath, "paras.xml")
    
        
        
if __name__ == '__main__':
        #pp = ParametersPlatform("C:\\Users\\el\\Desktop\\configuration.xml")
        #paras = pp.GetTaskParameters("0")
        #print paras.iden + "," + paras.user + "," + paras.password + "," + paras.queryType
        """
        result = FuncParaParser("crcQuer, para, para2, 3, 4")
        for para in result:
            print para
            """
        pp = ParametersPlatform("C:\\Users\\el\\Desktop\\")
            
        print pp.GetAllTheradsNames()
            
            
            
            
            
            
            
            
            
            