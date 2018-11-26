import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, DateTime, Time
from database import db

class TradePrice(db.Model):
    __tablename__ = 'TradePrice'
    id = Column(Integer, primary_key=True)

    high = Column(Float)
    low = Column(Float)
    vol = Column(Float)
    last = Column(Float)
    buy = Column(Float)
    sell = Column(Float)
    date = Column(DateTime)
    website = Column(String(120))
    SetCoin = Column(String(20))
    BuyCoin = Column(String(20))

    def __init__(self):
        pass

    def __repr__(self):
        return '<title %r>' % (self.title)


class PriceNode(db.Model):
    __tablename__ = 'PriceNode'
    priceNodeId = Column(Integer, primary_key=True)

    price = Column(Float)

    timeutc = Column(Time)

    website = Column(String(120))

    sellPrice = Column(Float)

    butPrice = Column(Float)

    def __init__(self):
        pass


    def __repr__(self):
        return '<title %r>' % (self.title)
