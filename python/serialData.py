import sys
import time
import json

class serialData:

    dataFilePath = ""
    dataFile = ""
    data = []

    flowCount = 0;
    flowLevel = 5;

    def __init__(self,dataFilePath):
        print "init" , dataFilePath
        self.dataFilePath = dataFilePath
        self.dataFile = self.dataFilePath + "data_" + time.strftime("%Y%m%d") + ".json"
        print self.dataFile


    def load(self):
        print "dataFile loading..."
        print self.dataFilePath
        self.dataFile = self.dataFilePath + "data_" + time.strftime("%Y%m%d") + ".json"
        print self.dataFile
        with open(self.dataFile,'r') as jsonFile:
            try:
                print "loading"
                self.data = json.load(jsonFile)
                print self.data
                return self.data
            except Exception, Argument:
                print 'Json Load Error:',Argument

    def store(self):
        try:
            print "dataFile store"
            print self.dataFilePath
            print self.dataFile
            with open(self.dataFile,'w') as jsonFile:
                jsonFile.write(json.dump(self.data));
                #jsonFile.write(data);
        except Exception, Argument:
            print 'store Error:',Argument

    def append(self, data):
        try:
            print 'appding',len(self.data)
            if len(self.data) == 0:
                self.load()
            print 'appding self'
            try:
                self.data.append(data)
            except Exception, Argument:
                print 'append list Error:',Argument
            self.flowCount += 1
            if(self.flowCount >= self.flowLevel):
                self.flowCount = 0
                self.store();
        except Exception, Argument:
            print 'append list Error EE:',Argument

    def serialTrade(self,data):
        print "dataFile serialTrade"
        self.store(data)
        print "load stored data file"
        d = self.load()
        print d
