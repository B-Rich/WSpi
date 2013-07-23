#!/usr/bin/env python
# -*- coding: utf-8 -*-

from weibo import APIClient
import webbrowser
import thread
theLock = thread.allocate_lock()

def GetClient(_key, _secret, _redirect_uri, userName, passWord):
    
    client = APIClient(app_key = _key, 
                       app_secret = _secret, 
                       redirect_uri = _redirect_uri)
    
    url = client.get_authorize_url()
    
    print "username:" + userName
    print "password:" + passWord
    print "threads blocked for login now"
    
    #multi-threads synchronize
    theLock.acquire()
    
    webbrowser.open_new(url)
    code = raw_input()
    
    theLock.release()
    #sync finished
    
    print "lock released"
    
    tok_class = client.request_access_token(code)
    token = tok_class.access_token
    expires = tok_class.expires_in
    
    client.set_access_token(token, expires)
    
    return client

if __name__ == '__main__':
    client = GetClient(_key="771437644", 
                       _secret="2801123737f2edf2c57201be1099ef7e", 
                       _redirect_uri="http://www.psych.ac.cn/")
    
    #result = client.statuses.user_timeline.get(uid=1848392535, screen_name="", count=100)
    #result = client.friendships.friends.get(uid = 1678998673, cursor = 0)
    """
    result = client.users.show.get(screen_name="青藏铁路")
    theid = result.id
    print str(theid)
    """
    
    count = 0
    cur = 0
    circle = 0
    while(True):
        circle += 1
        print str(circle)
        result = client.friendships.followers.active.get(uid = 2286736447, count = 200, cursor = cur)
        count += len(result.users)
        cur = count - 1
        
        if len(result.users) < 200:
            break
        
        if(circle > 100):
            break
        
    print "count:" + str(count)
    print "circle:" + str(circle)
    
    
    """
    for cons in result.statuses:
        print cons.text + " : " + str(cons.comments_count) + " : " + str(cons.attitudes_count) 
        """
    """
    for person in result.users:
        print person.screen_name
        """
        
    
        
    #print result.next_cursor
    #print result.previous_cursor        
    #print "count:" + str(len(result.statuses))
    