# Genesis_test_task

## Опис завдання
Потрібно реалізувати сервіс з АРІ, який дозволить:

- дізнатись поточний курс біткоіну (BTC) у гривні (UAH);
- підписати емейл на отримання інформації по зміні курсу;
- запит, який відправить всім підписаним користувачам актуальний курс.

## Виконання
Використовуєтьсяв Flask.<br>
Зробленні наступні файли:
- app/api/btc.py - реалізован API,
- app/coinmarketcap/cmc.py - работа з сайтом coinmarketcap.com,
- app/data/ - дерикторія для зберігання файлів з інформацією,
- app/main/email.py - запис, та разсикла email-ів,
- app/main/json_file.py - работа з файлами,
- app/tests/test_api.py
- app/config.py
- settings.py - початкові налаштування,
- web.py<br>
Також додані файли:
- docker-compose.yml
- Dockerfile

**Файл settings.py.**<br>
В ньому:
- EMAILS = 'emails.json', им'я файла для зберігання інформації.
- cryptosumbol = 'BTC' - символ криптоваоюти, яка нас цікавить.
- currency = 'UAH' - валюта до якої ми будимо отримувати курс 'BTC'.

**Потрібно зробити файл - .flaskenv,** в root дерікторії.<br>
В ньому зробити:
- FLASK_APP=web.py
- FLASK_DEBUG=1
- ENVIRONMENT=development
- SECRET_KEY=<some_secret_key>

- API_COINMARCETCAP=<api_key для доступу к coinmarketcap.com>.

- EMAIL=<xxxx - email, якій буде використано для разсилкі почти>.
- EMAIL_PASSWORD=<xxxx - пароль до email, якій буде використано для разсилкі почти>.


**Є наступні перевірки.**
- корректний нам надіслан email. чи ні.
- чи є директорія та файл де зберігається інформація.
- чи порожній файл з інформацією.




