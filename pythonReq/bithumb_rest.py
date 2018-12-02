import httplib2
import os
import sys
import json
import time
from urllib import parse  # import urlencode
from database import db_session, db
from stageData import dataSchema
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from config import Config
import time
from datetime import datetime
TradePrice = dataSchema.TradePrice

from . import RestJson
from . import SerialTicker
ticker = RestJson.ticker
tickerJson = RestJson.tickerJson
InitFlask = SerialTicker.InitFlask


def tickerBtc():
    rootUrl = "https://api.bithumb.com/public/ticker/{}"

    url = rootUrl.format("btc")
    return ticker(url, True)


def TradeTicker(length, timespan):
    priceArray = []
    InitFlask()

    for i in range(length):
        time.sleep(timespan)
        jsonData = tickerBtc()
        priceArray.append(TickerModel_Bithumb(jsonData, "BTC", "KRW"))

        if len(priceArray > 50):
            db.session.add_all(priceArray)
            db.session.commit()
            priceArray.clear()

    db.session.add_all(priceArray)
    db.session.commit()


'''
{
    "status":"0000",
    "data":{"opening_price":"4798000","closing_price":"4699000","min_price":"4613000",
        "max_price":"4848000","average_price":"4721120.5644","units_traded":"3356.83438328",
        "volume_1day":"3356.83438328","volume_7day":"39533.29830293","buy_price":"4693000",
        "sell_price":"4700000","24H_fluctate":"-99000","24H_fluctate_rate":"-2.06","date":"1543774665386"
    }
}
'''
def TickerModel_Bithumb(jsonData, setCoin, buyCoin):
    site = "bithumb"
    status = jsonData["status"]
    print(status)
    jsonTicker = jsonData["data"]
    tp = TradePrice()
    tickerDate = jsonTicker["date"]
    print(tickerDate, int(tickerDate))
    tp.date = datetime.fromtimestamp(int(tickerDate))
    tp.high = float(jsonTicker['max_price'])
    tp.low = float(jsonTicker['min_price'])
    tp.vol = float(jsonTicker['volume_1day'])
    tp.last = float(jsonTicker['buy_price'])
    tp.buy = float(jsonTicker['buy_price'])
    tp.sell = float(jsonTicker['sell_price'])
    tp.website = site
    tp.SetCoin = setCoin
    tp.BuyCoin = buyCoin
    return tp