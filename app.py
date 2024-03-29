import os
import constantes

from flask_session import Session
from flask_bootstrap import Bootstrap5
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, constantes.DATABASE_NAME)}"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from visualizar_Restaurantes import *
from visualizar_Usuario import *
from visualizar_Pratos import *
from visualizar_Conta import *
from visualizar_Pesquisa import *