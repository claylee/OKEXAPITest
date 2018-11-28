from stageData import dataSchema
from . import performData
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash,jsonify
from pythonReq import okcoinRest
from Util.JsonEncoderCustom import JsonCustomEncoder, AlchemyEncoder
import json
from . import fomula
import numpy as np
import time
import datetime
TradePrice = dataSchema.TradePrice

#TODO:
@performData.route("/", methods=["GET", "POST"])
def index():
    content = okcoinRest.realTrades()
    return render_template("performData/index.html", json=content)


@performData.route("/OKEx", methods=["GET", "POST"])
def showOKEx():
    content = okcoinRest.realTrades()
    return render_template("performData/OKEx.html", tradeContent=content)


@performData.route("/tickers", methods=["GET", "POST"])
def tickers():
    tickList = TradePrice.query.all()
    return render_template("performData/tickers.html", tickers=tickList)


@performData.route("/line", methods=["GET", "POST"])
def line():
    tickList = TradePrice.query.all()
    arr,dictHour = fomula.ConstructTensor(tickList)
    x = arr[:, 1]
    x[x==0] = 4000
    y = arr[:, 2]
    y[y==0] = 30
    a = x[0]/y[0]
    t = x - y * a
    return render_template(
        "performData/linechart.html",
        jsondata=json.dumps(list(arr[:, 0])),
        line1=json.dumps(list(x/y-a)),
        line2=json.dumps(list(y- x/a)),
        hour1 = json.dumps(dictHour))



@performData.route("/dateticker/", methods=["GET", "POST"])
@performData.route("/dateticker/<day>/<hour>", methods=["GET", "POST"])
def DateTicker(day = None ,hour = None):
    print(day)

    if day is None:
        line = TradePrice.query.all()
        arr,dictHour = fomula.ConstructTensor(line)
        return jsonify(dictHour)
        
    dt = datetime.datetime.strptime(day, "%Y-%m-%d");
    now_time = datetime.datetime.now()
    print(dt)
    print(now_time)
    print(now_time + datetime.timedelta(days=-1))
    timespam = time.mktime(dt.timetuple())
    print(timespam)
    print(dt+datetime.timedelta(days = 1))
    timespam2 = time.mktime((dt+datetime.timedelta(days = 1)).timetuple())
    print(timespam , timespam2)

    print(datetime.datetime.fromtimestamp(int(timespam))
        , datetime.datetime.fromtimestamp(int(timespam2)))


    line = TradePrice.query.filter(TradePrice.date >= dt,TradePrice.date <= dt+datetime.timedelta(days = 1)).all()
    print(line)
    arr,dictHour = fomula.ConstructTensor(line)
    x = arr[:, 1]
    x[x==0] = 4000
    y = arr[:, 2]
    y[y==0] = 30
    a = x[0]/y[0]
    t = x - y * a
    for i in dictHour:
        for j in dictHour[i]:
            data = dictHour[i][j]
            arrNp1 = np.array(data[0])
            arrNp2 = np.array(data[1])
            a = arrNp1[0]/arrNp2[0]
            data[0] = list(arrNp1/arrNp2 - a)
            data[1] = list(arrNp2 - arrNp1/a)
    return jsonify(dictHour)
