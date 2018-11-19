import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from database import db

class PriceNode():
    __tablename__ = 'PriceNode'
    priceNodeId = Column(Integer, primary_key=True)
    price = Column(Number)

    timeutc = Column(DateTime)

    website = Column(String(120))

    sellPrice = Column(Number)

    butPrice = Column(Number)

    def __init__(self):
        pass


    def __repr__(self):
        return '<title %r>' % (self.title)


class DataSchema():

    price = 0
    CoinType = ""
