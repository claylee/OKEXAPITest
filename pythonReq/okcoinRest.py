
import httplib2
import os
import sys
import json
import time
from urllib import parse # import urlencode
from database import db_session,db
from stageData import dataSchema
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from config import Config
import time

TradePrice = dataSchema.TradePrice

def buildSign():
    pass

def StartApp():
    app = Flask(__name__)
    sys.path.append("..\\..\\")

    Config.SQLALCHEMY_DATABASE_URI = 'sqlite:///../tmp/coin.db'

    app.config.from_object(Config)
    print(Config)
    app.app_context().push()
    with app.app_context():
        print("-------------------------")
        db.init_app(app)
    print(db.get_app())
    TradeCoins(2000,5)

def TradeCoins(length,timespan):
    coins = ['ltc','btc']
    tradeUrl = "https://www.okcoin.com/api/v1/ticker.do?symbol={}_{}"

    tickerCache = {}
    print(db)
    print(db.get_app())

    for c in coins:
        tickerCache[c] = []

    for l in range(length):
        time.sleep(timespan)
        print('..')
        for c in coins:
            try:
                url = tradeUrl.format(c,"usd")
                #{"date":"1543211767","ticker":{"high":"31.93","vol":"2227.00","last":"31.06","low":"26.24","buy":"31.02","sell":"31.06"}}
                jsonData = ticker(url)
                print(jsonData["ticker"])
                tickerCache[c].append(TickerModel(jsonData,"okcoin",c,"USD"))
                print(c,len(tickerCache[c]))
                if(len(tickerCache[c]) > 50):
                    print("-- alchemy serial")
                    db.session.add_all(tickerCache[c])
                    db.session.commit()
                    tickerCache[c].clear()
                    #tickerCache[c] = []
            except Exception as ex:
                print(ex)

    for c in coins:
        db.session.add_all(tickerCache[c])
        db.session.commit()


def TickerModel(jsonData,site,SetCoin,BuyCoin):
    tickerDate = jsonData["date"]
    jsonTicker = jsonData["ticker"]
    tp = TradePrice()
    tp.date = time.localtime(int(tickerDate))
    tp.high = float(jsonTicker['high'])
    tp.low = float(jsonTicker['low'])
    tp.vol = float(jsonTicker['vol'])
    tp.last = float(jsonTicker['last'])
    tp.buy = float(jsonTicker['buy'])
    tp.sell = float(jsonTicker['sell'])
    tp.website = site
    tp.SetCoin = SetCoin
    tp.BuyCoin = BuyCoin
    return tp

def ticker(url):
    con = httplib2.Http()
    body_data = {};
    body = parse.urlencode(body_data)

    header_data = {'Content-Type': 'application/x-www-form-urlencoded'}

    resp, content = con.request(url,method="GET",body=body,headers=header_data)

    return json.loads(content)




def realTrades():
    tradeUrl = "https://www.okcoin.com/api/v1/ticker.do?symbol=ltc_usd"
    con = httplib2.Http()
    body_data = {};
    body = parse.urlencode(body_data)

    header_data = {'Content-Type': 'application/x-www-form-urlencoded'}

    dbRange = []
    for i in range(80):
        resp, content = con.request(tradeUrl,method="GET",body=body,headers=header_data)
        tp = TradePrice()
        jsonContent = None
        print(content.decode())
        jsonContent = json.loads(content)
        ticker = jsonContent['ticker']
        print(ticker['high'])
        tp.high = float(ticker['high'])
        tp.low = float(ticker['low'])
        tp.vol = float(ticker['vol'])
        tp.last = float(ticker['last'])
        tp.buy = float(ticker['buy'])
        tp.sell = float(ticker['sell'])
        tp.website = "okcoin"
        tp.SetCoin = "LTC"
        tp.BuyCoin = "USD"
        dbRange.append(tp)
        time.sleep(1)

    db.session.add_all(dbRange)
    db.session.commit()


    return content
