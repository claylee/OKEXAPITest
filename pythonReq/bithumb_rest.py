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

def tickerBtc():
    rootUrl = "https://api.bithumb.com/public/ticker/{}"

    baseurl = rootUrl.format("btc")
    return ticker(url)


def ticker(url):
    con = httplib2.Http()
    body_data = {}
    body = parse.urlencode(body_data)

    header_data = {'Content-Type': 'application/x-www-form-urlencoded'}

    resp, content = con.request(url, method="GET", body=body, headers=header_data)

    return json.loads(content)