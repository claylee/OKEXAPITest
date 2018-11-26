
import httplib2
import json
from urllib import parse # import urlencode
from database import db
from stageData import dataSchema
import time

TradePrice = dataSchema.TradePrice

def buildSign():
    pass

def TradeCoins(length,timespan):
    coins = ['ltc','btc']
    tradeUrl = "https://www.okcoin.com/api/v1/ticker.do?symbol={}_{}"

    tickerCache = {}

    for c in coins:
        tickerCache[c] = []

    for l in range(length):
        time.sleep(timespan)
        for c in coins:
            try:
                url = tradeUrl.format(c,"usd")
                jsonTicker = ticker(url)
                print(jsonTicker["ticker"])
                tickerCache[c].append(TickerModel(jsonTicker["ticker"],"okcoin",c,"USD"))
                if(len(tickerCache[c]) > 200):
                    db.session.add_all(tickerCache[c])
                    db.session.commit()
                    tickerCache[c] = []
            except ex as Exception:
                print(ex)

    for c in coins:
        db.session.add_all(tickerCache[c])
        db.session.commit()


def TickerModel(jsonTicker,site,SetCoin,BuyCoin):
    tp = TradePrice()
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
