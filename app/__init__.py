from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

import views, models