'''
Created on 2013-7-3

@author: el
'''
import time

def Bar(interval, pinterval, threadID):
    tstart = time.time()
    print threadID + ": start to wait..."
    while(True):
        elapsed = time.time() - tstart 
        if elapsed > interval:
            break
        else:
            print threadID + ": %d second(s) left" % (round(interval - elapsed))
            time.sleep(pinterval)
    print threadID + ": waiting is over."
    

        
if __name__ == '__main__':
    Bar(interval = 20, pinterval = 1)
    
    
    
    
    