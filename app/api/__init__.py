""""""
from flask_restful import Api

from app.api.btc import Btc, Email, SendBtc


def init_app(app):
    with app.app_context():
        api = Api(app)
        api.add_resource(Btc, '/api/rate/')
        api.add_resource(Email, '/api/subscribe/')
        api.add_resource(SendBtc, '/api/sendEmails/')

