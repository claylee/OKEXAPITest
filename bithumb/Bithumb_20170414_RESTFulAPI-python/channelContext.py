import sys
import time
import json
import sqlite3

class channelContext:
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

    def sqlJsonConnection(self, createtable):
        print('sqlJsonConnection')
        conn = sqlite3.connect(self.rootDir + '/test.db')
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

    def store(self):
        try:
            print('store')
            s = "INSERT INTO bithumbTick VALUES (?,?,?,?,?,?,?,?,?,?,?)"
            print(s)
            with self.sqlJsonConnection(True) as conn:
                print("ssss")
                for jsonrow in self.jsonData["data"]:
                    print(jsonrow.values())
                    conn.execute(s, tuple(jsonrow.values()))

            with open(self.filename,'w+') as jsonFile:
                json.dump(self.jsonData,jsonFile)
                jsonFile.close()
        except Exception as Argument:
            print('store Error:',Argument)
