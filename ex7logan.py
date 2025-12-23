from datetime import datetime
import copy

class logAnalyzer:
    
    log = []
    structuredLog = []
    ipList = []
    timeList = []
    uniqueIPList = []
    methodList = []
    methods = {"GET": 0, "POST": 0, "PATCH": 0, "PUT": 0, "DELETE": 0, "TRACE": 0, "CONNECT": 0, "HEAD": 0, "OPTIONS": 0}
    URLDict = {}
    peakTime = {}
    highestHour = -1
    bruteLog = {}
    
    def __init__(self,logName):
        self.logName = logName
        
    
    
    def docReader(self):
        list = []
    
        try:
            with open(self.logName, "r") as log:
                for line in log:
                    list.append(line)
        except FileNotFoundError:
            print("The file was nout found, exiting...")

        self.log = list


    def getStructuredLog(self):
        structuredPreLog = []
        for line in self.log:
            for word in line.split():
                structuredPreLog.append(word)
            self.structuredLog.append(structuredPreLog)
            structuredPreLog = []
        print(self.structuredLog)
        
    
    
    
    def getIpFromLog(self):
        for ipAdress in self.structuredLog:
            self.ipList.append(ipAdress[0])
    
        print("Carsten LIST: ", self.ipList)




    def getTime(self):
        for time in self.structuredLog:
            time = time[3]
            time = time[1:]
            self.timeList.append(time)
        
        print("TIME LIST: ", self.timeList)




    def getRest(list):
        restList = []
        for rest in list:
            rest = rest.strip()
            restList.append(rest[48:len(rest)])
    
        return restList

    




    def getUniqueIP(self):
        uniqueIpList = []
        for ip in self.ipList:
            if ip not in uniqueIpList:
                uniqueIpList.append(ip)

    
        print("UNIQUE IP LIST: ", uniqueIpList)
    
    

    def getMethods(self):
        for method in self.structuredLog:
            method = method[5]
            method = method[1:]
            self.methodList.append(method)
        print(self.methodList)

    def getTotalRequestsPerMethod(self):
        for method in self.methodList:
            if method not in self.methods.keys():
                self.methods.add(method, 1)
            else:
                self.methods[method] = self.methods[method] + 1
                
        print(self.methods)

    def getMostRequestedURL(self):
        highest = 0
        for method in self.structuredLog:
            method = method[7]
            if method in self.URLDict.keys():
                self.URLDict[method] = self.URLDict[method] + 1
            else:
                self.URLDict[method] = 1
      
        for element in self.URLDict:
            if self.URLDict[element] > highest:
                highest = self.URLDict[element]
                highestEntry = element
        

        print("highest Entry: ", highestEntry)
        
    
    
    def getPeakTrafficTimes(self):
        highest = 0
        highestPair = 0
        for time in self.timeList:
                datetime_object = datetime.strptime(time, '%d/%b/%Y:%H:%M:%S')
                hour = datetime_object.time().hour
                if hour not in self.peakTime:
                    self.peakTime[hour] = 1
                
                else:
                    self.peakTime[hour] = self.peakTime[hour] + 1
                
    
        for element in self.peakTime.keys():
            print("ELEMENT: ", element)
            print(self.peakTime[element])
            if self.peakTime[element] > highest:
                highest = self.peakTime[element]
                highestKey = element
        
        self.highestHour = highestKey
        print("highest: ", highestKey, "'o clock", "with ", highest, " requests")

    
    def getFailedAttempts(self):
        failedAttempt = 0
        for attempt in self.structuredLog:
            if 199 < int(attempt[8]) < 399:
                print("succesful try with errorCode: ", attempt[8])
            
            elif int(attempt[8]) == 403:
                print("Forbidden access attempt by IP:", attempt[0])
            else:
                print("failed Login Attempt by IP: ", attempt[0], "with ErrorCode: ", attempt[8])
                if attempt[0] not in self.bruteLog.keys():
                    self.bruteLog[attempt[0]] = 1
                   
                else:
                    self.bruteLog[attempt[0]] = self.bruteLog[attempt[0]] + 1
        
        tempLog = copy.deepcopy(self.bruteLog)
        for pair in self.bruteLog:
            if self.bruteLog[pair] < 2:
                del tempLog[pair]
            
        self.bruteLog = tempLog
        print("BruteForce Log (IP/Failed Attempts > 1)", self.bruteLog)
    
    
    def genFiles(self):
        try:
            with open("sumary_report.txt", "w") as summary:
                summary.write("Summary \n")
                summary.write("IP LIST \n")
                for line in self.ipList:
                  
                        summary.write(line + "\n")
                        
                summary.write("TIME LIST \n")
                for line in self.timeList:
                  
                        summary.write(line + "\n")
                        
           
                
                summary.write("METHOD  LIST \n")
                for line in self.methodList:
                  
                        summary.write(line + "\n")
                        
                        
        except FileNotFoundError:
                        print("The file was not found, exiting...")

        
        
        
analysis = logAnalyzer("example_log.txt")
print(analysis.logName)
analysis.docReader()
analysis.getStructuredLog()
analysis.getIpFromLog()
analysis.getTime()
analysis.getUniqueIP()
analysis.getMethods()
analysis.getTotalRequestsPerMethod()
analysis.getMostRequestedURL()
analysis.getPeakTrafficTimes()
analysis.getFailedAttempts()
analysis.genFiles()

# Output Files to Generate
# summary_report.txt - Overall statistics and high-level findings1.
# security_incidents.txt - Detailed list of security-relevant events2.
# error_log.txt - All HTTP errors (4xx and 5xx status codes)3.
# analysis_audit.log - Your programme's logging output documenting the analysis process

