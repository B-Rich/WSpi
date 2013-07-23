'''
Created on 2013-6-24

@author: el
'''

from DataLayer import DBMySQLDriver
import DBNames
import re

class DBOps:
    
    def __init__(self, parahost, parauser, parapass, paraport, paradbname):
        #initialize dbDriver
        self.mDBDriver = DBMySQLDriver.DBMySQLDriver(
                        _host=parahost, _user=parauser, 
                        _pass=parapass, _port=paraport, _dbname=paradbname)
        
        #if database not exists create one and build tables
        if self.mDBDriver.DBExists(paradbname) == False:
            self.mDBDriver.CreateDataBase()
            self.buildTables()
            
        self.VOID = "void"
    
    def makeCreatTableColumnsClause(self, fieldTuple):
        clause = ""
        
        i = 0
        for field in fieldTuple:
            clause += field
            if(i != len(fieldTuple) - 1):
                clause += ","
            i += 1
            
        return clause
    
    def makeInsertTableColumnsClause(self, fieldTuple):
        clause = ""
        
        i = 0
        for field in fieldTuple:
            clause += self.trim4Fieldname(text=field)
            if(i != len(fieldTuple) - 1):
                clause += ", "
            i += 1
            
        return clause
    
    def trim4Fieldname(self, text):
        rex = re.compile("\S+")
        mt = rex.match(text)
        return mt.group(0)
    
    def createSubTab(self):
        self.mDBDriver.CreateTable(
            tableName = DBNames.SubTabName, 
            columns = self.makeCreatTableColumnsClause(fieldTuple = DBNames.SubTabFields))
    
    def createStaTab(self):
        self.mDBDriver.CreateTable(
            tableName = DBNames.StaTabName,
            columns = self.makeCreatTableColumnsClause(fieldTuple = DBNames.StaTabFields))
        
    def createCommTab(self):
        self.mDBDriver.CreateTable(
            tableName = DBNames.CommTabName,
            columns = self.makeCreatTableColumnsClause(fieldTuple = DBNames.CommTabFields),
            FKclause = DBNames.CommTabFKClause)
        
    def createMassTab(self):
        self.mDBDriver.CreateTable(
            tableName = DBNames.MassTabName,
            columns = self.makeCreatTableColumnsClause(fieldTuple = DBNames.MassTabFields))
        
    def createRltTab(self):
        self.mDBDriver.CreateTable(
            tableName = DBNames.RltTabName, 
            columns = self.makeCreatTableColumnsClause(fieldTuple = DBNames.RltTabFields), 
            FKclause = DBNames.RltTabFKClause)
     
    def buildTables(self):
        self.createSubTab()
        self.createStaTab()
        self.createCommTab()
        self.createMassTab()
        self.createRltTab()
    
    def genUpdateStrFieldStr(self, fieldstr, value):
        retval = self.trim4Fieldname(fieldstr) 
        retval += u" = '" 
        retval += value + u"'"
            
        return retval
    
    def genUpdateBoolFieldStr(self, fieldstr, value):
        retval = self.trim4Fieldname(fieldstr) + " = " + "'" + str(value) + "'"
        return retval
    
    def genUpdateIntFieldStr(self, fieldstr, value):
        retval = self.trim4Fieldname(fieldstr) + " = " + str(value)
        return retval
    
    def getVoidToleStr(self, content):
        if not content or content == "''":
            return "-4"
        else:
            return content
    
    def getSubRecUpdateScheme(self, info):
        infolist = []
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[1], value=info.screen_name))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[2], value=info.name))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[3], value=info.province))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[4], value=info.city))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[5], value=info.location))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[6], value=(info.description).replace("'", " ")))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[7], value=info.url))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[8], value=info.profile_image_url))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[9], value=info.domain))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[10], value=info.gender))
        infolist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.SubTabFields[11], value=info.followers_count))
        infolist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.SubTabFields[12], value=info.friends_count))
        infolist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.SubTabFields[13], value=info.statuses_count))
        infolist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.SubTabFields[14], value=info.favourites_count))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[15], value=info.created_at))
        infolist.append(self.genUpdateBoolFieldStr(fieldstr=DBNames.SubTabFields[16], value=info.following))
        infolist.append(self.genUpdateBoolFieldStr(fieldstr=DBNames.SubTabFields[17], value=info.allow_all_act_msg))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[18], value=info.remark))
        infolist.append(self.genUpdateBoolFieldStr(fieldstr=DBNames.SubTabFields[19], value=info.geo_enabled))
        infolist.append(self.genUpdateBoolFieldStr(fieldstr=DBNames.SubTabFields[20], value=info.verified))
        infolist.append(self.genUpdateBoolFieldStr(fieldstr=DBNames.SubTabFields[21], value=info.follow_me))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.SubTabFields[22], value=str(info.online_status)))
        infolist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.SubTabFields[23], value=info.bi_followers_count))
        retval = ", ".join(infolist)
        return retval
    
    def getStaRecUpdateScheme(self, info):
        fieldlist = []
        fieldlist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.StaTabFields[1], value=info.created_at))
        fieldlist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.StaTabFields[2], value=(info.text).replace(u"'", u" ")))
        fieldlist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.StaTabFields[3], value=(info.source).replace(u"'", u" ")))
        fieldlist.append(self.genUpdateBoolFieldStr(fieldstr=DBNames.StaTabFields[4], value=info.favorited))
        fieldlist.append(self.genUpdateBoolFieldStr(fieldstr=DBNames.StaTabFields[5], value=info.truncated))
        fieldlist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.StaTabFields[6], value=self.getVoidToleStr(info.in_reply_to_status_id)))
        fieldlist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.StaTabFields[7], value=self.getVoidToleStr(info.in_reply_to_user_id)))
        fieldlist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.StaTabFields[8], value=self.getVoidToleStr(info.in_reply_to_screen_name)))
        fieldlist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.StaTabFields[9], value=info.mid))
        fieldlist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.StaTabFields[10], value=info.reposts_count))
        fieldlist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.StaTabFields[11], value=info.comments_count))
        fieldlist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.StaTabFields[12], value=info.attitudes_count))
        fieldlist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.StaTabFields[13], value=info.user.id))
        retval = ", ".join(fieldlist)
        return retval
    
    def getCommRecUpdateScheme(self, info):
        infolist = []
        
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.CommTabFields[1], value=info.created_at))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.CommTabFields[2], value=(info.text).replace("'", " ")))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.CommTabFields[3], value=(info.source).replace("'", " ")))
        infolist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.CommTabFields[4], value=info.mid))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.CommTabFields[5], value=info.user.id))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.CommTabFields[6], value=info.status.id))
        retval = ", ".join(infolist)
        return retval
    
    def getRltRecUpdateScheme(self, subinfo, objinfo, additionalInfo):
        infolist = []
        infolist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.RltTabFields[1], value=str(subinfo.id)))
        infolist.append(self.genUpdateIntFieldStr(fieldstr=DBNames.RltTabFields[2], value=str(objinfo.id)))
        infolist.append(self.genUpdateBoolFieldStr(fieldstr=DBNames.RltTabFields[3], value=str(subinfo.following)))
        infolist.append(self.genUpdateBoolFieldStr(fieldstr=DBNames.RltTabFields[4], value=str(subinfo.followed_by)))
        infolist.append(self.genUpdateStrFieldStr(fieldstr=DBNames.RltTabFields[5], value=additionalInfo))
        retval = ", ".join(infolist)
        return retval
    
    def getSubRecInsertValueScheme(self, info):
        fieldList = []
        fieldList.append(str(info.id))
        fieldList.append("'" + info.screen_name + "'")
        fieldList.append("'" + info.name + "'")
        fieldList.append("'" + info.province + "'")
        fieldList.append("'" + info.city + "'")
        fieldList.append("'" + info.location + "'")
        fieldList.append("'" + (info.description).replace("'", " ") + "'")
        fieldList.append("'" + info.url + "'")
        fieldList.append("'" + info.profile_image_url + "'")
        fieldList.append("'" + info.domain + "'")
        fieldList.append("'" + info.gender + "'")
        fieldList.append(str(info.followers_count))
        fieldList.append(str(info.friends_count))
        fieldList.append(str(info.statuses_count))
        fieldList.append(str(info.favourites_count))
        fieldList.append("'" + info.created_at + "'")
        fieldList.append("'" + str(info.following)  + "'")
        fieldList.append("'" + str(info.allow_all_act_msg) + "'")
        fieldList.append("'" + info.remark + "'")
        fieldList.append("'" + str(info.geo_enabled) + "'")
        fieldList.append("'" + str(info.verified) + "'")
        fieldList.append("'" + str(info.follow_me) + "'")
        fieldList.append("'" + str(info.online_status) + "'")
        fieldList.append(str(info.bi_followers_count))
        retval = ", ".join(fieldList)
        return retval
    
    def getStaRecInsertValuesScheme(self, info):
        fieldlist = []
        fieldlist.append(str(info.id))
        fieldlist.append("'" + info.created_at + "'")
        fieldlist.append(self.getVoidToleStr("'" + (info.text).replace("'", " ") + "'"))
        fieldlist.append(self.getVoidToleStr("'" + (info.source).replace("'", " ") + "'"))
        fieldlist.append("'" + str(info.favorited) + "'")
        fieldlist.append("'" + str(info.truncated) + "'")
        fieldlist.append(self.getVoidToleStr(str(info.in_reply_to_status_id)))
        fieldlist.append(self.getVoidToleStr(str(info.in_reply_to_user_id)))
        fieldlist.append(self.getVoidToleStr("'" + info.in_reply_to_screen_name + "'"))
        fieldlist.append(str(info.mid))
        fieldlist.append(str(info.reposts_count))
        fieldlist.append(str(info.comments_count))
        fieldlist.append(str(info.attitudes_count))
        fieldlist.append(str(info.user.id))
        #print fieldlist[2]
        retval = ", ".join(fieldlist)
        return retval
    
    def getCommRecInsertValuesScheme(self, info):
        infolist = []
        infolist.append(str(info.id))
        infolist.append("'" + info.created_at + "'")
        infolist.append("'" + info.text.replace("'", " ") + "'")
        infolist.append("'" + info.source.replace("'", " ") + "'")
        infolist.append(str(info.mid))
        infolist.append(str(info.user.id))
        infolist.append(str(info.status.id))
        retval = ", ".join(infolist)
        return retval
    
    def getRltInsertValueScheme(self, subinfo, objinfo, addInfo):
        infolist = []
        infolist.append("'" + str(subinfo.id) + str(objinfo.id) + "'")
        infolist.append(str(subinfo.id))
        infolist.append(str(objinfo.id))
        infolist.append("'" + str(subinfo.following) + "'")
        infolist.append("'" + str(subinfo.followed_by) + "'")
        infolist.append("'" + addInfo + "'")
        retval = ", ".join(infolist)
        return retval
        
    
    #if exists: update
    #from weibo structure 2 database directly
    def PutSubRecord(self, info):
        #update
        if self.mDBDriver.RecExists(tableName=DBNames.SubTabName, 
            fieldKey=self.trim4Fieldname(DBNames.SubTabFields[0]), fieldValue=info.id):
            self.mDBDriver.UpdateRecord(tableName=DBNames.SubTabName, 
                updateClause=self.getSubRecUpdateScheme(info=info),
                condition=self.trim4Fieldname(text=DBNames.SubTabFields[0]) + " = " + str(info.id))
        else:#insertion
            self.mDBDriver.InsertRecord(tableName=DBNames.SubTabName, 
                columns=self.makeInsertTableColumnsClause(fieldTuple=DBNames.SubTabFields), 
                values=self.getSubRecInsertValueScheme(info=info))
    
    def PutStaRecord(self, info):
        if self.mDBDriver.RecExists(tableName=DBNames.StaTabName, 
            fieldKey=self.trim4Fieldname(DBNames.StaTabFields[0]), fieldValue=info.id):
            #update
            self.mDBDriver.UpdateRecord(tableName=DBNames.StaTabName,
                updateClause=self.getStaRecUpdateScheme(info=info),
                condition=self.trim4Fieldname(text=DBNames.StaTabFields[0]) + " = " + str(info.id))
        else:#insertion
            self.mDBDriver.InsertRecord(tableName=DBNames.StaTabName, 
                columns=self.makeInsertTableColumnsClause(fieldTuple=DBNames.StaTabFields), 
                values=self.getStaRecInsertValuesScheme(info=info))
            
    def PutCommRecord(self, info):
        if self.mDBDriver.RecExists(tableName=DBNames.CommTabName, 
            fieldKey=self.trim4Fieldname(text=DBNames.CommTabFields[0]), fieldValue=info.id):
            #update
            self.mDBDriver.UpdateRecord(tableName=DBNames.CommTabName, 
                updateClause=self.getCommRecUpdateScheme(info=info), 
                condition=self.trim4Fieldname(text=DBNames.CommTabFields[0]) + "=" + str(info.id))
        else:
            #insertion
            self.mDBDriver.InsertRecord(tableName=DBNames.CommTabName, 
                columns=self.makeInsertTableColumnsClause(fieldTuple=DBNames.CommTabFields), 
                values=self.getCommRecInsertValuesScheme(info=info))
        
    def PutMassRecord(self, info, grpText):
        if self.mDBDriver.RecExists(tableName=DBNames.MassTabName, 
            fieldKey=self.trim4Fieldname(DBNames.MassTabFields[0]), fieldValue=info.id):#update
            self.mDBDriver.UpdateRecord(tableName=DBNames.MassTabName, 
                updateClause=self.getSubRecUpdateScheme(info=info) + ", " +self.genUpdateStrFieldStr(fieldstr=DBNames.MassTabFields[24], value=grpText),
                condition=self.trim4Fieldname(text=DBNames.MassTabFields[0]) + " = " + str(info.id))
        else:#insertion
            self.mDBDriver.InsertRecord(tableName=DBNames.MassTabName, 
                columns=self.makeInsertTableColumnsClause(fieldTuple=DBNames.MassTabFields), 
                values=self.getSubRecInsertValueScheme(info=info) + ", '" + grpText + "'")
            
    #primary key: subid string + objid string
    def PutRltRecord(self, sub_info, obj_info, additionalInfo="void"):
        if self.mDBDriver.RecExists(tableName=DBNames.RltTabName, 
            fieldKey=self.trim4Fieldname(DBNames.RltTabFields[0]), fieldValue=(str(sub_info.id) + str(obj_info.id))):#update
            self.mDBDriver.UpdateRecord(tableName=DBNames.RltTabName, 
            updateClause=self.getRltRecUpdateScheme(subinfo=sub_info, objinfo=obj_info, additionalInfo=additionalInfo), 
            condition=self.trim4Fieldname(text=DBNames.RltTabFields[0]) + " = " + str(sub_info.id) + str(obj_info.id))
        else:#insert
            self.mDBDriver.InsertRecord(tableName=DBNames.RltTabName, 
                columns=self.makeInsertTableColumnsClause(fieldTuple=DBNames.RltTabFields), 
                values=self.getRltInsertValueScheme(subinfo=sub_info, objinfo=obj_info, addInfo=additionalInfo))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                