import os
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config.from_object(config)

db = SQLAlchemy(app)
migate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

Bootstrap(app)

from app.models import user, post
from app.routes import index