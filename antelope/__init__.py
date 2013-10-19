from flask import Flask, Blueprint, render_template, url_for, request
from flask.ext.mongoengine import MongoEngine
from flask.views import MethodView
from jinja2 import FileSystemLoader
import datetime
import os

root = os.path.abspath(os.path.dirname(__file__) + '/../')

app = Flask(__name__, static_folder='../static', static_url_path='/static')
app.config["MONGODB_SETTINGS"] = {'DB': "antelope_finance"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
# set our template path
app.jinja_loader = FileSystemLoader(os.path.join(root, 'templates'))

db = MongoEngine(app)
user = "isaac"

from antelope import views, models
