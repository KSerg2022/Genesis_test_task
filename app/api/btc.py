"""API"""
from flask_restful import Resource, reqparse
from flask import make_response, jsonify

from app.coinmarketcap.cmc import Cmc
from app.main.email import AddEmail, SendEmail


class Base(Resource):

    @staticmethod
    def get_disable():
        """HTTP method GET disable."""
        response = {'message': 'method "GET" is disable.'}
        return make_response(jsonify(response), 200)

    @staticmethod
    def post_disable():
        """HTTP method POST disable."""
        response = {'message': 'method "POST" is disable.'}
        return make_response(jsonify(response), 200)

    @staticmethod
    def put_disable():
        """HTTP method PUT disable."""
        response = {'message': 'method "PUT" is disable.'}
        return make_response(jsonify(response), 200)

    @staticmethod
    def delete_disable():
        """HTTP method DELETE disable."""
        response = {'message': 'method "DELETE" is disable.'}
        return make_response(jsonify(response), 200)


class Btc(Base):
    """
    API for get BTC rate to UAH.
    /api/rate/.
    GET = BTC rate to UAH; 200.
    """
    def __init__(self):
        self.btc = None

    def get(self):
        """HTTP method GET"""
        self.btc = Cmc().get_cryptocurrency()
        try:
            message = self.btc['message']
            response = self.btc
            return make_response(jsonify(response), 400)
        except (TypeError, KeyError):
            return make_response(jsonify({'rate': round(float(self.btc['price']), 3)}), 200)

    def post(self):
        """HTTP method POST"""
        return self.post_disable()

    def put(self):
        """HTTP method PUT"""
        return self.put_disable()

    def delete(self):
        """HTTP method DELETE"""
        return self.delete_disable()


class Email(Base):
    """
    API for adding Email to file.
    /api/subscribe/.
    POST = BTC rate to UAH; 200.
    """
    def __init__(self):
        self.status = None
        self.request = None
        self.regparse = reqparse.RequestParser()
        self.regparse.add_argument('name',
                                   type=str,
                                   required=True,
                                   location='json')

    def post(self):
        """HTTP method POST."""
        self.request = self.regparse.parse_args()
        self.request.name = self.request.name.capitalize()

        add_email = AddEmail()
        self.status = add_email.check_email_in_file(self.request.name)
        try:
            message = self.status['message']
            response = self.status
            return make_response(jsonify(response), 409)
        except (TypeError, KeyError):
            response = {'message': 'E-mail додано'}
            return make_response(jsonify(response), 200)

    def get(self):
        """HTTP method GET"""
        return self.get_disable()

    def put(self):
        """HTTP method PUT"""
        return self.put_disable()

    def delete(self):
        """HTTP method DELETE"""
        return self.delete_disable()


class SendBtc(Base):
    """
    API for sending Emails.
    /api/sendEmails/.
    POST = BTC rate to UAH; 200.
    """
    def __init__(self):
        self.email = None
        self.status = None

    def post(self):
        """HTTP method POST."""
        add_email = SendEmail()
        self.status = add_email.send_emails()

        try:
            message = self.status['message']
            response = self.status
            return make_response(jsonify(response), 409)
        except (TypeError, KeyError):
            response = {'message': 'E-mail-и відправлено'}
            return make_response(jsonify(response), 200)

    def get(self):
        """HTTP method GET"""
        return self.get_disable()

    def put(self):
        """HTTP method PUT"""
        return self.put_disable()

    def delete(self):
        """HTTP method DELETE"""
        return self.delete_disable()
