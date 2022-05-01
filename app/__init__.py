from flask_bootstrap import Bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__,template_folder='templates')
    app.config['SECRET_KEY']='B!1weNAt1T^%'
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@127.0.0.1:3306/bdvacunatorio' 
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'vacunatorioing2g36@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Ingenieria2'
    Bootstrap(app)
    db.init_app(app)
    return app