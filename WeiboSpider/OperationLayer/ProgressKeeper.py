'''
Created on 2013-7-3

@author: el
'''

import os
import re

class ProgressKeeper:
    def __init__(self, basepath, threadID):
        self.mPath = GetProgressFileName(basePath=basepath, threadID=threadID)
        
    def WriteProgress(self, progressArr):
        fp = os.open(filename=self.mPath, flag="w")
        
        for para in progressArr:
            fp.write(para + ", ")
        
        fp.close()
        
    def ReadProgress(self):
        fp = os.open(filename=self.mPath, flag="r")
        content = fp.read() 
        fp.close()
        
        rex = re.compile("\w+")
        return rex.findall(content)
        
    
        
    
            
def GetProgressFileName(basePath, threadID):
    return os.path.join(basePath, threadID)
        

if __name__ == '__main__':
    pass