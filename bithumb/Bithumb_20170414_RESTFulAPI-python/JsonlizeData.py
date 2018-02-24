

import sys
import time
import json
import channelContext

class JsonlizeData:
    dataFilePath = ""
    dataFile = ""
    data = {"channel":"","data":[]}

    flowCount = 0;
    flowLevel = 50;

    channelDict = {}

    def __init__(self,dataFilePath):
        print("init" , dataFilePath)
        self.dataFilePath = dataFilePath
        self.data = {"channel":"","data":[]}
        self.dataFile = self.dataFilePath + "data_" + time.strftime("%Y%m%d") + ".json"
        print(self.dataFile)


    def load(self,items):
        print("----dataFile loading...")
        self.dataFile = self.dataFilePath + "data_" + items["channel"]+"_"+ time.strftime("%Y%m%d") + ".json"
        return self.loadData()

    def loadData(self):
        print("----dataFile loading...")
        with open(self.dataFile,'a+') as jsonFile:
            try:
                print("loading")
                loaddata = json.load(jsonFile)
                if(loaddata != None and "status" in loaddata.data):
                    self.data = loaddata
                jsonFile.close()
                return self.data
            except Exception as Argument:
                print('Json Load Error:',Argument)

    def store(self):
        try:
            print("----dataFile store")
            print(self.dataFile,self.data)
            with open(self.dataFile,'w+') as jsonFile:
                #jsonFile.write(json.dumps(self.data));
                json.dump(self.data,jsonFile)
                #jsonFile.write(data);
                jsonFile.close()
        except Exception as Argument:
            print('store Error:',Argument)

    def SerialMessage(self,message):
        chlCtx = None
        #print(message)
        c = message["status"]
        #print(c)
        try:
            if(c in self.channelDict):
                chlCtx = self.channelDict[c]
            else:
                chlCtx = channelContext.channelContext(self.dataFilePath,message)
                self.channelDict[c] = chlCtx
                chlCtx.load(c)

            #print(self.channelDict[c])
            chlCtx.addItem(message["data"]);
            print(chlCtx)

            self.flowCount += 1
            print(" | ",self.flowCount,self.flowLevel)
            if(self.flowCount >= self.flowLevel):
                print(" > ",self.flowCount,self.flowLevel)
                self.flowCount = 0
                chlCtx.store();
        except Exception as Argument:
            print('SerialMessage Error:',Argument)


    def append(self, data):
        try:
            print('----appding',len(self.data))
            newDataItem = data['data']
            DataItemChannel = data['channel']
            CurrentChannel = self.data["channel"]
            print("Channel",CurrentChannel,DataItemChannel)
            if(DataItemChannel != CurrentChannel):
                #print('load item channel changed')
                self.store();
                self.load(data)

            if(self.data == None or self.data["channel"] == ""):
                ###print('load item')
                self.load(data)
            print("!!!",self.data)
            try:
                JsonItems = self.data['data']
                self.data["channel"] = DataItemChannel
                JsonItems.extend(newDataItem)
            except Exception as Argument:
                print('append list Error:',Argument)
            self.flowCount += 1
            print(" | ",self.flowCount,self.flowLevel)
            if(self.flowCount >= self.flowLevel):
                print(" > ",self.flowCount,self.flowLevel)
                self.flowCount = 0
                self.store();
        except Exception as Argument:
            print('append list Error EE:',Argument)

    def serialTrade(self,data):
        print("----dataFile serialTrade")
        self.store(data)
        print("load stored data file")
        d = self.load(data)
