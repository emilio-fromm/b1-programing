logis = [
("alice", "success"),
("bob", "failed"),
("bob", "failed"),
("charlie", "success"),
("bob", "failed"),
("alice", "failed")]

logCountN = []
logCountT = []
for logTupel in logis:
   
   if logTupel not in logCountT and logTupel[1] == "failed":
        logCountT.append(logTupel)
        logCountN.append([logTupel[0], logis.count(logTupel)])
        
        if logis.count(logTupel) > 2:
            print(logTupel[0], " Access denied! - You have too many login attempts!!")
        

        
    
   


print(logCountN)


