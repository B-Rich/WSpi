'''
Created on 2013-6-24

@author: el

congregated operations

'''

from FunctionLayer import DBOps
from DataLayer import ClientFactory
import time

class AtomOps:
    def __init__(self, parameters):
        
        self.mThreadParas = parameters
        
        self.mClient = ClientFactory.GetClient(_key=self.mThreadParas.appKey,
                                                _secret=self.mThreadParas.appSecret,
                                                _redirect_uri=self.mThreadParas.callbackAddr,
                                                userName = self.mThreadParas.user,
                                                passWord = self.mThreadParas.password)
        
        self.mMySQLControl = DBOps.DBOps(parahost=self.mThreadParas.dbhost, parauser=self.mThreadParas.dbuser, 
                                   parapass = self.mThreadParas.dbpass, paraport=self.mThreadParas.dbport,
                                   paradbname=self.mThreadParas.dbname)
        
        self.mRequestCount = 0
        

    def FetchSubject(self, subname):
        user = self.mClient.users.show.get(screen_name=subname)
        self.mMySQLControl.PutSubRecord(info=user)
        return user.id
    
    def FetchMass(self, massid, note):
        mass = self.mClient.users.show.get(uid=massid)
        self.mMySQLControl.PutMassRecord(info=mass, grpText=note)
        return mass.id
    
    def LimitFetchBoardStatues(self, page):
        stas = self.mClient.statuses.friends_timeline.get(count=199, page=page)
        stasids = []
        for onesta in stas.statuses:
            self.mMySQLControl.PutStaRecord(info=onesta)
            stasids.append(onesta.id)
        
        print "$Fetched: " + len(stas.statuses)
    
    def FetchBoardStatuses(self, begpage, count):
        totalFetched = 0
        pageat = begpage
        stasids = []
        while(True):
            stas = self.mClient.statuses.friends_timeline.get(count=199, page=pageat)
            totalFetched += len(stas.statuses)
            
            pageat += 1
            
            for onesta in stas.statuses:
                self.mMySQLControl.PutStaRecord(info=onesta)
                stasids.append(onesta.id)
            
            print "$Fetched " + str(totalFetched) + "; page at: " + str(pageat)
               
            if totalFetched >= count:
                break
        
        return stasids
    
    #return request count
    def FetchStatusesOfUser(self, userid, frompage, topage):
        i = frompage
        stasids = []
        while(True):
            stas = self.mClient.statuses.user_timeline.get(uid = userid, count=199, page=i)
            time.sleep(1)
            
            print len(stas.statuses)
            
            for onesta in stas.statuses:
                self.mMySQLControl.PutStaRecord(info=onesta)
                stasids.append(onesta.id)
                
            i += 1
            
            #if len(stas.statuses) < 1:#less than thought finish
            #    toBreak = True
            
            if i == topage + 1:#formal finish
                break
            
        return stasids
    
    #return request count        
    def FetchCommentOfStatus(self, staid, begpage, count):
        i = 0
        totalFetched = 0
        thisFetched = 0
        while(True):
            
            comm = self.mClient.comments.show.get(id=staid, count=49, page=begpage, filter_by_author=0)
            
            for oneComm in comm.comments:
                self.mMySQLControl.PutCommRecord(info=oneComm)
            
            thisFetched = len(comm.comments)
            totalFetched += thisFetched 
            i += 1
            begpage += 1
            
            print thisFetched
            
            if totalFetched >= count:
                break
            
            if thisFetched == 0:
                break
            
        return i
    
    def FetchRelationship(self, subid, objid, note):
        rlt = self.mClient.friendships.show.get(source_id=subid, target_id=objid)
        self.mMySQLControl.PutRltRecord(sub_info=rlt.source, obj_info=rlt.target, additionalInfo=note)
        return None
    
if __name__ == '__main__':
    """
    from FunctionLayer import ParametersPlatform
    pp = ParametersPlatform.ParametersPlatform(_path="C:\\Users\\el\\Desktop\\")
    atomop = AtomOps(pp.GetTaskParameters(iden="0"))
    """
    #atomop.FetchSubject(subname="cookied")
    #atomop.FetchSubject(subname="Harbournne")
    
    #atomop.FetchStatusesOfUser(userid=1848392535, frompage=1, topage=3)
    #atomop.FetchBoardStatuses(begpage=1, count=300)
    #atomop.FetchCommentOfStatus(staid=3596759710361636, begpage=1, count=200)
    
    #atomop.FetchMass(massid=1848392535, note="me this is")
    
    #atomop.FetchRelationship(subid="1848392535", objid="1678998673", note="love")
    
    
           
    
        
        
        
        
        
        
