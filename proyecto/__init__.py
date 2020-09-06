from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='ad0197435a37654933c91669c1f51d26'
bcrypt= Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from proyecto import routes
