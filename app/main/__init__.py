import flask_monitoringdashboard as dashboard
from elasticsearch import Elasticsearch
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from app.main.admin import create_admin

from .config import config_by_name

db = SQLAlchemy(session_options={"expire_on_commit": False})
flask_bcrypt = Bcrypt()
es = Elasticsearch('http://elasticsearch:9200')
admin = Admin(name='jerkii', template_mode='bootstrap3')


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_by_name[config_name])

    app.config['FLASK_ADMIN_SWATCH'] = 'superhero'

    db.init_app(app)

    flask_bcrypt.init_app(app)

    dashboard.bind(app)
    dashboard.config.init_from(file="../../config.cfg")

    admin.init_app(app)
    create_admin(admin, db)


    return app
