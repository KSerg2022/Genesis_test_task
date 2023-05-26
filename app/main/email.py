"""
Modul for writing emails to file and sending emails to addresses from file with information about rate BTC.
"""
import os
import re
from flask_mail import Mail, Message
from typing import Match

from app.main.json_file import JsonFile


mail = Mail()
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    # "MAIL_PORT": 587,
    # "MAIL_USE_TLS": True,
    # "MAIL_USE_SSL": False,

    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv('EMAIL'),
    "MAIL_PASSWORD": os.getenv('EMAIL_PASSWORD')
}


class Email:
    KEY = 'emails'
    value = []

    def __init__(self):
        self.json = JsonFile()

    def get_emails(self) -> bool | list[str]:
        """Load emails from file."""
        emails = self.json.load_data_from_file()
        if not emails:
            return False
        return list(emails.values())[0]


class AddEmail(Email):
    """Wright imail to file."""

    def check_email_in_file(self, email: str) -> bool | dict:

        if not self.verify_email(email):
            print({'message': 'email is not correct'})
            return {'message': 'email is not correct'}
        if not (emails := self.get_emails()):
            self.add_email(email)
        else:
            if email not in emails:
                emails.append(email)
                self.add_email(emails)
                return True

            print({'error': '409', 'description': 'Повертати, якщо e-mail вже є в базі даних (файловій)'})
            return {'message': 'Повертати, якщо e-mail вже є в базі даних (файловій)'}

    def add_email(self, emails: list | str) -> None:
        """Wright email to file."""
        self.json.dump_to_json(self.get_data_to_dump(emails))

    def get_data_to_dump(self, emails: list | str) -> dict[str, list[str]]:
        """Prepare data with emails to wright in file."""
        if isinstance(emails, str):
            return {self.KEY: [emails]}
        return {self.KEY: sorted(emails)}

    @staticmethod
    def verify_email(email: str) -> bool | Match[str]:
        """Verify email."""
        return re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)


class SendEmail(Email):
    """Send emails to addresses from file with information about rate BTC."""

    def __init__(self):
        super().__init__()
        self.sender = os.getenv('EMAIL')

    def send_emails(self) -> bool | dict:
        """Sending emails."""
        if not (emails := self.get_emails()):
            print({'message': 'Список електронных адрессов пуст.'})
            return {'message': 'Список електронных адрессов пуст.'}

        with mail.connect() as conn:
            for email in emails:
                message = 'Multy sending.'
                subject = "Hello from the other side!"
                msg = Message(subject=subject,
                              sender='mtk.09.2020@gmail.com',
                              recipients=[email],
                              body=message
                              )
                conn.send(msg)
        return True


if __name__ == '__main__':
    res = AddEmail()

    res.check_email_in_file('mtk.09.2020@gmail.com')
    res.check_email_in_file('koshevoys@gmail.com')
