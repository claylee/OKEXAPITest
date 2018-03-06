

import sys
import time
import json
import DbItemContext
import sqlite3

class SerialDataDb:
    dataFilePath = ""
    dataFile = ""
    dataFileDb = ""
    data = {"channel":"","data":[]}

    flowCount = 0;
    flowLevel = 20;

    channelDict = {}

    def __init__(self,dataFilePath):
        print("init" , dataFilePath)
        self.dataFilePath = dataFilePath
        self.data = {"channel":"","data":[]}
        self.dataFile = self.dataFilePath + "data_" + time.strftime("%Y%m%d") + ".json"
        self.dataFileDb = self.dataFilePath + "data_" + time.strftime("%Y%m%d") + ".db"
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

    def sqlJsonConnection(self, createtable):
        print('sqlJsonConnection')
        conn = sqlite3.connect(self.dataFileDb)
        print('sqlite3')
        if(createtable):
            print('createtable before')
            createTableSql = "create table IF NOT EXISTS bithumbTick( \
            tid INTEGER PRIMARY KEY AUTOINCREMENT \
            ,opening_price REAL,closing_price REAL \
            ,min_price REAL,max_price REAL,average_price REAL,units_traded REAL \
            ,volume_1day REAL,volume_7day REAL \
            ,buy_price REAL,sell_price REAL,date INTEGER)"
            print(createTableSql)
            conn.execute(createTableSql)
            print('createtable')
        return conn

    def SerialMessage(self,message):
        chlCtx = None
        #print(message)
        c = message["status"]
        #print(c)
        try:
            if(c in self.channelDict):
                chlCtx = self.channelDict[c]
            else:
                chlCtx = DbItemContext.DbItemContext(self.dataFilePath,message)
                self.channelDict[c] = chlCtx
                chlCtx.load(c)

            #print(self.channelDict[c])
            chlCtx.addItem(message["data"]);
            #print(chlCtx)

            self.flowCount += 1
            print(" | ",self.flowCount,self.flowLevel)
            if(self.flowCount >= self.flowLevel):
                print(" > ",self.flowCount,self.flowLevel)
                self.flowCount = 0
                self.store(chlCtx);
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

    def storeToFile(self):
        try:
            print("----storeToFile store")
            print(self.dataFile,self.data)
            with self.sqlJsonConnection(True) as conn:
                with open(self.dataFile,'w+') as jsonFile:
                    #jsonFile.write(json.dumps(self.data));
                    cursor = conn.cursor();
                    cursor.execute("SELECT opening_price ,closing_price  \
                    ,min_price ,max_price ,average_price ,units_traded  \
                    ,volume_1day ,volume_7day ,buy_price ,sell_price \
                    FROM bithumbTick")
                    self.data["data"] = cursor.fetchall()
                    print self.data
                    json.dump(self.data,jsonFile)
                    #jsonFile.write(data);
                    jsonFile.close()
        except Exception as Argument:
            print('storeToFile:',Argument)
        self.dataFile

    def store(self, dataContext):
        try:
            print('store')
            s = "INSERT INTO bithumbTick (opening_price ,closing_price  \
            ,min_price ,max_price ,average_price ,units_traded  \
            ,volume_1day ,volume_7day ,buy_price ,sell_price ,date \
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
            print(s)
            jsonData = dataContext.jsonData["data"]
            with self.sqlJsonConnection(True) as conn:
                print("ssss")
                for jsonrow in jsonData:
                    print(jsonrow.values())
                    conn.execute(s, tuple(jsonrow.values()))
                conn.commit()
                dataContext.clearItems()

        except Exception as Argument:
            print('store Error:',Argument)
