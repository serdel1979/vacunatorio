from flask_bootstrap import Bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__,template_folder='templates')
    app.config['SECRET_KEY']='B!1weNAt1T^%'
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:admin@127.0.0.1:3306/bdvacunatorio'
    Bootstrap(app)
    db.init_app(app)
    return app