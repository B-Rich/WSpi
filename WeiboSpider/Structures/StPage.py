'''
Created on 2013-7-18

@author: el
'''

class st_user:
    id = -1
    screen_name = "void"
    name = "void"
    province = "void"
    city = "void"
    location = "void"
    description = "void"
    url = "void"
    profile_image_url = "void"
    domain = "void"
    gender = "void"
    followers_count = -1
    friends_count = -1
    statuses_count = -1
    favourites_count = -1
    created_at = -1
    following = -1
    allow_all_act_msg = False
    remark = "void"
    geo_enabled = False
    verified = False
    follow_me = False
    online_status = -1
    bi_followers_count = -1

class st_status:
    id = -1
    created_at = "-1"
    source = "void"
    text = "void"
    mid = -1
    idstr = "-1"
    favorited = False
    truncated = False
    in_reply_to_status_id = "-1"
    in_reply_to_user_id = "-1"
    in_reply_to_screen_name = "void"
    reposts_count = -1
    comments_count = -1
    attitudes_count = -1
    user = st_user()
    
    
    