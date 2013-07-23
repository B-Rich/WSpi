'''
Created on 2013-7-3

@author: el
'''

from FunctionLayer import ParametersPlatform
import AtomOps
import string
import TimeBar
import ProgressKeeper

def RunScheme(tup_paras):
    basepath = tup_paras[0]
    paras = tup_paras[1]
    func = ParametersPlatform.FuncParaParser(paras.queryClause)
    bar = TimeBar(3600, 15, tup_paras[1].iden)
    progress = ProgressKeeper(basepath, paras.iden)
    
    
    """
    subject, subname, statuses_from_page, statuses_to_page
    if-carrryover, time-control, query-loops 
    """
    if(func[0] == "subject"):
        querycount = 0
        atom = AtomOps(tup_paras)
        #get subject
        uid = atom.FetchSubject(func[1])
        querycount += 1 
        
        #if carryover
        stasids = []
        #get statuses
        if(paras.carryover == "False"):
            stasids = atom.FetchStatusesOfUser(userid=uid, frompage = func[2], topage = func[3])
            querycount += (string.atoi(func[3]) - string.atoi(func[2]) + 1)
        else:#carryover
            stasids = progress.ReadProgress()
        
        #get comments
        for one_id in stasids:
            count = atom.FetchCommentOfStatus(one_id)
            querycount += count
            #sleep when over the limit
            if(querycount >= string.atoi(paras.requestPerHour)):
                bar.Bar()
                querycount = 0
                leftids = stasids.range(stasids.index(one_id), len(stasids))
                progress.write(leftids)
            
            
            
            
            
            
            
            
            
            
            
            
            
