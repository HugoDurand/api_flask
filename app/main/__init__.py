import flask_monitoringdashboard as dashboard
from elasticsearch import Elasticsearch
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name

db = SQLAlchemy(session_options={"expire_on_commit": False})
flask_bcrypt = Bcrypt()
es = Elasticsearch('http://elasticsearch:9200')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    dashboard.bind(app)
    dashboard.config.init_from(file="../../config.cfg")

    return app
