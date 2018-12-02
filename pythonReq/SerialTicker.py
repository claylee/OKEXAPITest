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

tickerCache = []


def SaveModel(modelArray):
    app = InitFlask()

    for l in range(len(modelArray)):

        for c in coins:
            try:
                tickerCache[c].append(
                    TickerModel(jsonData, "okcoin", c, "USD"))
                print(c, len(tickerCache[c]))
                if (len(tickerCache[c]) > 50):
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

def MultiPost(modelArray):
    db.session.add_all(modelArray)
    db.session.commit()



def InitFlask():
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
    return app