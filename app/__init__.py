""""""
from flask import Flask


from app.main.email import mail, mail_settings
from app.config import config
from app.api import init_app as init_app_btc


def create_app(config_name='default'):
    # регистрация (инициализация) app
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.config.update(mail_settings)
    mail.init_app(app)

    init_app_btc(app)


    return app

