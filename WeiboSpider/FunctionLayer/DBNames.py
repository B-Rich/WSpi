'''
Created on 2013-6-24

@author: el

global static variables
'''

#APP_KEY = "771437644"
#SECRET = "2801123737f2edf2c57201be1099ef7e"
#CALLBACK_ADDR = "http://www.psych.ac.cn/"

SubTabName = "SUBJECTS"
SubTabFields = ("ID BIGINT PRIMARY KEY", 
                "SCREEN_NAME TINYTEXT", 
                "NAME TINYTEXT", 
                "PROVINCE TINYTEXT", 
                "CITY TINYTEXT", 
                "LOCATION TINYTEXT", 
                "DESCRIPTION TINYTEXT", 
                "URL TEXT", 
                "PROFILE_IMAGE_URL TEXT", 
                "DOMAIN TINYTEXT", 
                "GENDER VARCHAR(32)", 
                "FOLLOWERS_COUNT INT", 
                "FRIENDS_COUNT INT", 
                "STATUSES_COUNT INT", 
                "FAVORITE_COUNT INT", 
                "CREATED_AT TINYTEXT", 
                "FOLLOWING VARCHAR(32)", 
                "ALLOW_ALL_ACT_MSG VARCHAR(32)", 
                "REMARK TINYTEXT", 
                "GEO_ENABLED VARCHAR(32)", 
                "VERIFIED VARCHAR(32)", 
                "FOLLOW_ME VARCHAR(32)", 
                "ONLINE_STATUS VARCHAR(32)", 
                "BI_FOLLOWERS_COUNT INT")

StaTabName = "STATUSES"
StaTabFields = ("ID BIGINT PRIMARY KEY",
                "CREATED_AT TINYTEXT", 
                "TEXT TEXT", 
                "SOURCE TINYTEXT", 
                "FAVORITED VARCHAR(32)", 
                "TRUNCATED VARCHAR(32)", 
                "IN_REPLY_TO_STATUS_ID BIGINT",
                "IN_REPLY_TO_USER_ID BIGINT", 
                "IN_REPLY_TO_SCREEN_NAME TINYTEXT", 
                "MID BIGINT", 
                "REPOSTS_COUNT INT",
                "COMMENTS_COUNT INT", 
                "ATTITUDES_COUNT INT", 
                "USER_ID BIGINT")
#StaTabFKClause = "CONSTRAINT USER_ID_FK FOREIGN KEY (USER_ID) REFERENCES " + SubTabName + " (ID)"

CommTabName = "COMMENTS"
CommTabFields = ("ID BIGINT PRIMARY KEY", 
                 "CREATED_AT TINYTEXT", 
                 "TEXT TEXT", 
                 "SOURCE TINYTEXT", 
                 "MID BIGINT", 
                 "USER_ID BIGINT", 
                 "STATUS_ID BIGINT")
CommTabFKClause = ", FOREIGN KEY (STATUS_ID) REFERENCES " + StaTabName + " (ID) ON DELETE CASCADE"

MassTabName = "MASSES"
MassTabFields = ("ID BIGINT PRIMARY KEY", 
                "SCREEN_NAME TINYTEXT", 
                "NAME TINYTEXT", 
                "PROVINCE TINYTEXT", 
                "CITY TINYTEXT", 
                "LOCATION TINYTEXT", 
                "DESCRIPTION TINYTEXT", 
                "URL TEXT", 
                "PROFILE_IMAGE_URL TEXT", 
                "DOMAIN TINYTEXT", 
                "GENDER VARCHAR(32)", 
                "FOLLOWERS_COUNT INT", 
                "FRIENDS_COUNT INT", 
                "STATUSES_COUNT INT", 
                "FAVORITE_COUNT INT", 
                "CREATED_AT TINYTEXT", 
                "FOLLOWING VARCHAR(32)", 
                "ALLOW_ALL_ACT_MSG VARCHAR(32)", 
                "REMARK TINYTEXT", 
                "GEO_ENABLED VARCHAR(32)", 
                "VERIFIED VARCHAR(32)", 
                "FOLLOW_ME VARCHAR(32)", 
                "ONLINE_STATUS VARCHAR(32)", 
                "BI_FOLLOWERS_COUNT INT",
                "GROUP_MARK TINYTEXT")

RltTabName = "RELATIONSHIPS"
RltTabFields = ("ID VARCHAR(255) PRIMARY KEY",
                "SUBJECT_ID BIGINT", 
                "OBJECT_ID BIGINT", 
                "FOLLOW VARCHAR(32)", 
                "BE_FOLLOWED VARCHAR(32)", 
                "ADDTIONAL_INFO TINYTEXT")
RltTabFKClause = ", FOREIGN KEY (SUBJECT_ID) REFERENCES " + SubTabName + " (ID) ON DELETE CASCADE"

