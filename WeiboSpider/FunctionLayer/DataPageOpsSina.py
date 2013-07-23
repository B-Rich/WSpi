'''
Created on 2013-6-27

@author: el
'''

from DataLayer import ClientFactory
import DBOps

class DataPageOps:
    def __init__(self, appKey, appSecret, redirectURI, host, user, passwd, port, dbname):
        self.mClient = ClientFactory.GetClient(
        _key=appKey, _secret=appSecret, _redirect_uri=redirectURI)
        
        self.mDB = DBOps.DBOps(
                    parahost=host, parauser=user, parapass=passwd, paraport=port, paradbname=dbname)
        
    def SaveStaPageData(self, sub_screen_name, user_id=0, pagenum=1, rec_perpg=200, since_id=0):
        result = self.mClient.statuses.user_timeline.get(
            screen_name=sub_screen_name, pagenum=pagenum, count=rec_perpg, since_id=since_id)
        
        for rec in result.statuses:
            self.mDB.InsertStaRecord(rec)
        
        return None
    
    def SaveCommPageData(self, staid, count=50, page=1):
        result = self.mClient.comments.show(id=staid, count=count, page=page)
        
        for rec in result.comments:
            self.mDB.insertCommRecord(rec)
            
    def SaveFollowingMassPageData(self, sub_screen_name, count=200, begpos):
        result = self.mClient.friendships.friends(screen_name=sub_screen_name, count=count, cursor=begpos)
        
        for rec in result.users:
            self.mDB.InsertMassRecord(rec)
            
    def SaveFansMassPageData(self, sub_screen_name, count=200, begpos):
        result = self.mClient.friendships.followers(screen_name=sub_screen_name, count=count, cursor=begpos)
        
        for rec in result.users:
            self.mDB.InsertMassRecord(rec)
        
        

if __name__ == '__main__':
    pass