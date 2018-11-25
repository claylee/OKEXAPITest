import sys
import time
import json

class channelContext:
    channel = ""
    filename = ""

    rootDir = ""

    jsonData = {"channel":"","data":[]}

    def __init__(self,rootdir,message):
        print "---channelContext init"
        self.rootDir=rootdir
        self.channel = message["channel"]
        self.filename = self.rootDir + "data_" +self.channel +"_"+ time.strftime("%Y%m%d") + ".json"


    def load(self, channel):
        return self.loadData()

    def loadData(self):
        with open(self.filename,'r') as jsonFile:
            try:
                loaddata = json.load(jsonFile)
                if(loaddata != None and loaddata.has_key("channel")):
                    self.jsonData = loaddata
                jsonFile.close()
                return self.jsonData
            except Exception, Argument:
                print 'Json Load Error:',Argument

    def addItem(self,item):
        self.jsonData["data"].extend(item)

    def store(self):
        try:
            with open(self.filename,'w+') as jsonFile:
                json.dump(self.jsonData,jsonFile)
                jsonFile.close()
        except Exception, Argument:
            print 'store Error:',Argument
