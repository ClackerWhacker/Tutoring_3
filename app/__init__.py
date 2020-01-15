from flask import Flask
from flask_mail import Mail
import os
import config

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config["debug"] = False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'boyns12345@gmail.com'
app.config['MAIL_PASSWORD'] = 'Edelman1993'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config.from_object(config.Config)

mail = Mail(app)


from app import routes