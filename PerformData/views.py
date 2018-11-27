from stageData import dataSchema
from . import performData
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from pythonReq import okcoinRest
from Util.JsonEncoderCustom import JsonCustomEncoder, AlchemyEncoder
import json
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
    return render_template(
        "performData/linechart.html",
        jsondata=json.dumps(tickList, cls=AlchemyEncoder))
