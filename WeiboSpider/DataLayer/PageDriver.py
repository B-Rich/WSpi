'''
Created on 2013-7-18

@author: el
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#!/usr/bin/python2.7 
# -*- coding: utf-8 -*- 

import time
import string
import re

def rollBottom(driver):#javascript
    src = '''(function () 
    {
        var y = 0, step = 2500; 
        window.scroll(0, 0); 
        function oneRoll() 
        { 
            if(y < document.body.scrollHeight)
            {
                y += step; 
                window.scroll(0, y); 
                setTimeout(oneRoll, 3000);
            }  
            else 
            { 
                window.scroll(0, 0); 
            } 
        } 
        setTimeout(oneRoll, 1000);
    })();'''
            
    driver.execute_script(src)
    
def rollTo(driver, elem):
    driver.execute_script("arguments[0].scrollIntoView();", elem)

def login(driver, usernm, passwd):
    node_username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pl_login_form"]/div[1]/div/input')))
    node_username.send_keys(usernm)
    #node_username.submit()
    
    node_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pl_login_form"]/div[2]/div/input')))
    node_password.send_keys(passwd)
    #node_password.submit()
    
    node_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="pl_login_form"]/div[6]/a/span')))
    node_login.click()

def getStaElems(driver):
    midNode = driver.find_elements_by_css_selector('div.WB_feed_type.SW_fun')
    return midNode

def getText(staElem):
    textNodes = staElem.find_elements_by_css_selector('div.WB_text')
    
    tlist = []
    for node in textNodes:
        tlist.append(node.text)
        
    retval = ''.join(tlist)
        
    return retval
    #txtNode = driver.find_element(By.XPATH, xpath)
    #driver.execute_script("arguments[0].scrollIntoView();", txtNode)
    #return txtNode.text
    
def getMid(elem):
    try:
        mid = elem.get_attribute("mid")
        retval = string.atol(mid)
    except:
        retval = -1
        
    return retval

def getTime(staElem):
    try:
        timeNode = staElem.find_element_by_css_selector('a.S_link2.WB_time')
        time = timeNode.get_attribute("title")
        time = time.replace('-', '')
        time = time.replace(':', '')
        time = time.replace(' ', '')
    except:
        time = "void"
    return time

def getRepostsCount(staElem): 
    try:   
        rcNode = staElem.find_element_by_css_selector('a[action-type="feed_list_forward"]')#find_element(By.XPATH, xpath)
        rcStr = rcNode.text
        pat = re.compile('\\d+')
        mt = pat.findall(rcStr)
        if len(mt) > 0:
            retval = string.atoi(mt[0])
            return retval
        else:
            return 0
    except:
            return -1

def getCommentCount(staElem):
    try:
        commNode = staElem.find_element_by_css_selector('a[action-type="feed_list_comment"]')#driver.find_element(By.XPATH, xpath)
        commStr = commNode.text
        pat = re.compile('\\d+')
        mt = pat.findall(commStr)
        if len(mt) > 0:
            retval = string.atoi(mt[0])
            return retval
        else:
            return 0
    except:
            return -1

def gotoPeople(iden, driver):
    driver.get("http://www.weibo.com/u/" + str(iden))
    
def gotoPage(page, driver):
    driver.get(page)
    
def goNextPage(driver):
    try:
        pageControl = driver.find_element_by_css_selector('div.W_pages')
        btn = pageControl.find_element_by_css_selector('a[action-type=feed_list_page_next]')
        if btn:
            btn.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.WB_feed')))
            return True
        
        return False
    except:
        return False
        
if __name__ == '__main__':
    pass