"""
Module for working with the website coinmarketcap.com.
"""
import os

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dateutil import parser

from settings import cryptosumbol, currency

from dotenv import load_dotenv

load_dotenv()


class Cmc:

    def __init__(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'  # Latest quotes
        self.api_cmc = os.environ.get('API_COINMARCETCAP')

        self.parameters = {
            'symbol': cryptosumbol,
            'convert': currency
        }
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_cmc,
        }

    def get_cryptocurrency(self) -> dict[str, str] | bool:
        """
        Get information about cryptocurrency.
        """
        response = self.get_response()
        if response['status']['error_code']:
            print(response['status']['error_code'], response['status']['error_message'])
            return {'message': "Invalid status value"}

        cryptocurrency = self.parse_cryptocurrencies(response)
        return cryptocurrency

    def get_response(self) -> dict[dict]:
        """
        Make a request for site.
        """
        session = Session()
        session.headers.update(self.headers)

        try:
            response = session.get(self.url, params=self.parameters)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            message = f'openweathermap.org returned non-200 code. Actual code is: {response.status_code},' \
                      f' message is: {response.json()["status"]["error_message"]}'
            print('error ----- ', message)
            raise RuntimeError(message)

        session.close()
        return response.json()

    @staticmethod
    def parse_cryptocurrencies(currency_data: dict[dict]) -> bool | dict[str, str]:
        """Parse data."""
        try:
            currency_data['data'][cryptosumbol]
        except KeyError:
            print('Данные не lоступны. Попробуйте позже')
            return False

        return {
            'symbol': currency_data['status']['timestamp'],
            'name': currency_data['data'][cryptosumbol]['name'],
            'currency': list(currency_data['data'][cryptosumbol]['quote'].keys())[0],
            'price': currency_data['data'][cryptosumbol]['quote']['UAH']['price'],
            'data': parser.isoparse(currency_data['status']['timestamp']).strftime("%d-%m-%Y %H:%M:%S"),
        }
