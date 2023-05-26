"""
Json module.
"""
import json
import os

from json.decoder import JSONDecodeError

from settings import data_dir, EMAILS


class JsonFile:

    def __init__(self):
        self.path_to_file = data_dir / EMAILS

    def dump_to_json(self, data: dict) -> None:
        """Wright emails to jsonfile."""
        with open(self.path_to_file, 'w') as file_json:
            json.dump(data, file_json, indent=4)

    def load_data_from_file(self) -> dict:
        """Load emails from jsonfile."""
        self.check_file_exists()
        with open(self.path_to_file, 'r') as file_json:
            try:
                loaded_data = json.load(file_json)
                return loaded_data
            except JSONDecodeError:
                return {}

    def check_file_exists(self) -> None:
        """Check if file exists."""
        if not os.path.isdir(data_dir):
            os.mkdir(data_dir)

        if not os.path.isfile(self.path_to_file):
            with open(self.path_to_file, 'w'):
                pass
