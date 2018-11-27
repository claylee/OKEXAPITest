from flask import Flask
from stageData import dataSchema
from PerformData import fomula

from database import db_session, db
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from config import Config


def index(name=None):
    return render_template('index.html', name=name)


def test():
    app = Flask(__name__)

    app.config.from_object(Config)
    print(Config)
    app.app_context().push()
    with app.app_context():
        print("-------------------------")
        db.init_app(app)

    fomula.ConstructTensor()
