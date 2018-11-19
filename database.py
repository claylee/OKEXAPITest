#from sqlalchemy import create_engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
#from sqlalchemy.orm import scoped_session, sessionmaker
#from sqlalchemy.ext.declarative import declarative_base

#app.config['DATABASE'] = 'sqlite:////tmp/test.db'

#print("flask-sqlalchemy database url :",app.config['DATABASE'])
#print("flask-sqlalchemy database url :",app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy()
db_session = db.session

'''
# this block is SQLAlchemy API
engine = create_engine('sqlite:///tmp/flaskr.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # 在这里导入所有的可能与定义模型有关的模块，这样他们才会合适地
    # 在 metadata 中注册。否则，您将不得不在第一次执行 init_db() 时
    # 先导入他们。
    from models import category,document,picfile
    #print(category)
    Base.metadata.create_all(bind=engine)
'''

# below this is Flask-SQLAlchemy

def init_db():
    print("init db ")
    from stageData import dataSchema
    #from application import appc

    app = Flask(__name__)

    app.config.from_object(Config)
    #db.init_app(app)

    print(app.app_context())
    app.app_context().push()
    with app.app_context():
        print("-------------------------")
        db.init_app(app)
    print(app)
    db.create_all()
