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
tickerJson = RestJson.tickerJson
InitFlask = SerialTicker.InitFlask

from . import bithumb_rest as bithumb
from . import okcoinRest as okcoin


def tickerBtc():
    rootUrl = "https://api.bithumb.com/public/ticker/{}"

    url = rootUrl.format("btc")
    return ticker(url, True)


def TradeTicker(length, timespan):
    coinType = [[bithumb, "btc", "KRW", "bithumb"], [okcoin, "btc", "usd", "okcoin"]]
    priceArray = {}
    InitFlask()

    for i in range(length):
        time.sleep(timespan)
        for ctp in coinType:
            jsonData = ctp[0].ticker(ctp[1])
            print(jsonData)
            key = ctp[3] + "_" + ctp[1]
            if key not in priceArray:
                priceArray[key] = []
            priceArray[key].append(ctp[0].TickerModel(jsonData, ctp[3], ctp[1], ctp[2]))

            if len(priceArray[key]) > 50:
                db.session.add_all(priceArray[key])
                db.session.commit()
                priceArray[key].clear()

    for key in priceArray:
        array = priceArray[key]
        db.session.add_all(array)
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
