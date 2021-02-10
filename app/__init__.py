from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import makedirs

flask_app = Flask(__name__)
flask_app.config.from_pyfile("config.py", silent=True)

try:
    makedirs(flask_app.instance_path)
except OSError:
    pass

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)
csrf = CSRFProtect(flask_app)
login_manager = LoginManager()

csrf.init_app(flask_app)
login_manager.init_app(flask_app)

from app import models
from app.views import auth, dashboard

flask_app.register_blueprint(auth.bp)
flask_app.register_blueprint(dashboard.bp)

@flask_app.route("/")
def index():
    return redirect(url_for("auth.login"))