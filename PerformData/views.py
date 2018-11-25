from stageData import *
from . import performData
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from pythonReq import okcoinRest

@performData.route("/",methods=["GET","POST"])
def index():
    content = okcoinRest.realTrades()
    return render_template("performData/index.html",json = content)

@performData.route("/OKEx",methods=["GET","POST"])
def showOKEx():
    content = okcoinRest.realTrades()
    return render_template("performData/OKEx.html",tradeContent)
