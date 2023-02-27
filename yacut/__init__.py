from flask import Flask
from flask_sqlalchemy import Model, SQLAlchemy
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


from . import views, api_views, error_handlers, models
