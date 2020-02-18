from flask import Flask

# app init
app = Flask(__name__, instance_relative_config=True)


# load views
from app import views

#load config files
app.config.from_object('config')
