
import httplib2
import json
from urllib import parse # import urlencode
from database import db
from stageData import dataSchema
import time

TradePrice = dataSchema.TradePrice

def buildSign():
    pass

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
        print(content)
        jsonContent = None
        print(content.decode())
        jsonContent = json.loads(content)
        print(jsonContent)
        ticker = jsonContent['ticker']
        print(ticker['high'])
        tp.high = float(ticker['high'])
        tp.low = float(ticker['low'])
        tp.vol = float(ticker['vol'])
        tp.last = float(ticker['last'])
        tp.buy = float(ticker['buy'])
        tp.sell = float(ticker['sell'])
        dbRange.append(tp)
        time.sleep(1)

    db.session.add_all(dbRange)
    db.session.commit()


    return content
