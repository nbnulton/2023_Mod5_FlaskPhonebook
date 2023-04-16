from flask import Flask
#import class Config from config.py
from config import Config
# pulling from the routes.py
from.site.routes import site
#import authentication
from.authentication.routes import auth
from.api.routes import api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder


# running flask
app = Flask(__name__)
# CORS is a security, helps prevent cross-site request forgery
CORS(app)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)









