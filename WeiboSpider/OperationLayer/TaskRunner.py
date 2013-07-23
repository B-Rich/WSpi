'''
Created on 2013-7-3

@author: el
'''

import thread
import TaskScheme

from FunctionLayer import ParametersPlatform
from AtomOps import AtomOps

class TaskRunner:
    def __init__(self, basepath):
        self.mParasPlat = ParametersPlatform(_path = basepath)
        self.mBasePath = basepath
        
    def Run(self):
        allThreadsNames = self.mParasPlat.GetAllTheradsNames()
        for name in allThreadsNames:
            paras = self.mParasPlat.GetTaskParameters(name)
            thread.start_new_thread(TaskScheme.RunScheme, (self.mBasePath, paras))


if __name__ == '__main__':
    
    pp = ParametersPlatform.ParametersPlatform(_path="C:\\Users\\el\\Desktop\\")
    atomop = AtomOps(pp.GetTaskParameters(iden="0"))
    #atomop.LimitFetchBoardStatues(page=3)
    atomop.FetchRelationship(subid=1678998673, objid=1926222292, note="test")
    
    #atomop.FetchSubject(subname="cookied")
    #atomop.FetchSubject(subname="Harbournne")
    
    #atomop.FetchStatusesOfUser(userid=1848392535, frompage=1, topage=3)
    