'''
Created on 2013-7-18

@author: el
'''

from selenium import webdriver
from DataLayer import PageDriver
from Structures import StPage
import DBOps
import time

class Observation(object):
    '''
    observation
    '''
    def __init__(self, username, password):
        self.mDriver = webdriver.Chrome()
        self.mDriver.get('http://www.weibo.com')
        PageDriver.login(driver=self.mDriver, usernm=username, passwd=password)
        time.sleep(4)
        
    def gotoPeople(self, peopleNum):
        PageDriver.gotoPeople(iden=peopleNum, driver=self.mDriver)
        
    def gotoPage(self, pageAddr):
        PageDriver.gotoPage(page=pageAddr, driver=self.mDriver)
        
    def goNextPage(self):
        return PageDriver.goNextPage(driver=self.mDriver)
      
    def getURL(self):
        return self.mDriver.current_url
     
    def getCurPageSta(self, sleepDure):
        retval = []

        staElems = PageDriver.getStaElems(self.mDriver)
        addidx = 0
        while True:
            if len(staElems) > addidx:
                PageDriver.rollTo(driver=self.mDriver, elem=staElems[addidx])
                
                time.sleep(sleepDure)
                
                sta = StPage.st_status()
                sta.id = PageDriver.getMid(staElems[addidx])
                sta.idstr = str(sta.id)
                sta.mid = sta.id
                sta.created_at = PageDriver.getTime(staElems[addidx])
                sta.reposts_count = PageDriver.getRepostsCount(staElems[addidx])
                sta.comments_count = PageDriver.getCommentCount(staElems[addidx])
                sta.text = PageDriver.getText(staElems[addidx])
                #print(sta.text.encode('gbk', 'ignore'))
                retval.append(sta)
                addidx += 1
            else:#equals
                staElems = PageDriver.getStaElems(self.mDriver)
                if len(staElems) == addidx:
                    break
            
        return retval
    
    def quit(self):
        self.mDriver.quit()
        
if __name__ == '__main__':
    obs = Observation(username = "", password = "")
    #obs.gotoPeople("")
    obs.gotoPage("")
    
    #pp = ParametersPlatform.ParametersPlatform(_path="C:\\Users\\el\\Desktop\\")
    dbops = DBOps.DBOps(parahost="localhost", parauser="root", 
                                   parapass = "zxcvbnm", paraport="3306",
                                   paradbname="weibo")
    
    #obs.getCurPageSta()
    #print(obs.mDriver.page_source.encode('gbk', 'ignore'))
    while(True):
        pageStas = obs.getCurPageSta(sleepDure=0.5)
        
        for sta in pageStas:
            dbops.PutStaRecord(info=sta)
            
        if(obs.goNextPage()):
            time.sleep(5)
        else:
            print(obs.getURL())
            obs.quit()
            break;
        
        
        