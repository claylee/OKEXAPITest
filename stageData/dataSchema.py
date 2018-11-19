import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Time
from database import db

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
