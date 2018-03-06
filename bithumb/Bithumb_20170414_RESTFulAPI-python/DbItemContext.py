import sys
import time
import json
import sqlite3

class DbItemContext:
    channel = ""
    filename = ""

    rootDir = ""

    jsonData = {"status":"","data":[]}

    def __init__(self,rootdir,message):
        print("---channelContext init")
        self.rootDir=rootdir
        self.channel = message["status"]
        self.filename = self.rootDir + "data_" +self.channel +"_"+ time.strftime("%Y%m%d") + ".json"


    def load(self, channel):
        return self.loadData()

    def loadData(self):
        with open(self.filename,'a+') as jsonFile:
            try:
                loaddata = json.load(jsonFile)
                if(loaddata != None and "status" in loaddata):
                    self.jsonData = loaddata
                jsonFile.close()
                return self.jsonData
            except Exception as Argument:
                print('Json Load Error:',Argument)

    def addItem(self,item):
        self.jsonData["data"].append(item)

    def clearItems(self):
        self.jsonData["data"].clear()
