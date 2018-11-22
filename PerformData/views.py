from stageData import *
from . import performData
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash


@performData.route("/",methods=["GET","POST"])
def index():
    return render_template("performData/index.html")

@performData.route("/OKEx",methods=["GET","POST"])
def showOKEx():
    return render_template("performData/OKEx.html")
