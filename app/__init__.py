import os, sass
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

sass.compile(dirname=('app/static/scss', 'app/static/css'), output_style='compressed')
CORS(app, resources={r'/*': {'origins': '*'}})

from app import routes
