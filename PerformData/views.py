from stageData import dataSchema
from . import performData
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from pythonReq import okcoinRest
TradePrice = dataSchema.TradePrice

@performData.route("/",methods=["GET","POST"])
def index():
    content = okcoinRest.realTrades()
    return render_template("performData/index.html",json = content)

@performData.route("/OKEx",methods=["GET","POST"])
def showOKEx():
    content = okcoinRest.realTrades()
    return render_template("performData/OKEx.html",tradeContent)


@performData.route("/tickers",methods=["GET","POST"])
def tickers():
    tickList = TradePrice.query.all()
    return render_template("performData/tickers.html",tickers = tickList)
