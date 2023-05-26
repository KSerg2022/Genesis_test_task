import datetime

from pathlib import Path

base_dir = Path(__file__).parent
time_stamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

data_dir = base_dir / 'app' / 'data'


# file where stored emails addresses
EMAILS = 'emails.json'

cryptosumbol = 'BTC'
currency = 'UAH'
