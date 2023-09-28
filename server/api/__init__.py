
from flask import Flask, make_response,jsonify
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app= (app)
api = Api(app)


#
# con
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizza.db"
# initialize the app with the extension

from  api import routes
from api.models import db

migrate = Migrate(app, db)
db.init_app(app)