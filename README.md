# Genesis_test_task

*Очікувані мови виконання завдання: PHP, Go, JavaScript (Node.js).<br>
Виконувати завдання ***іншими мовами можна***, проте, це не буде перевагою.*

---

## Опис завдання
Потрібно реалізувати сервіс з АРІ, який дозволить:

- дізнатись поточний курс біткоїну (BTC) у гривні (UAH);
- підписати імейл на отримання інформації по зміні курсу;
- запит, який відправить всім підписаним користувачам актуальний курс.<br>
*Детальніше  у файлі - "SE'23 School_ Кейсове завдання.pdf"*

## Виконання
Використовуєтьсяв Flask.<br>
Зробленні наступні файли:
- app/api/btc.py - реалізовано API,
- app/coinmarketcap/cmc.py - робота з сайтом coinmarketcap.com,
- app/data/ - директорія для зберігання файлів з інформацією,
- app/main/email.py - запис, та розсилка email-ів. **Вікористовується сервіс Gmail.**
- app/main/json_file.py - робота з файлами,
- app/tests/test_api.py
- app/config.py
- settings.py - початкові налаштування,
- web.py<br>
Також додані файли:
- docker-compose.yml
- Dockerfile
- Dockerfile_win

**Файл settings.py.**<br>
В ньому:
- EMAILS = 'emails.json', ім'я файла для зберігання інформації.
- cryptosumbol = 'BTC' - символ криптовалюти, яка нас цікавить.
- currency = 'UAH' - валюта до якої ми будимо отримувати курс 'BTC'.

**Потрібно зробити файл - .flaskenv,** (см. *flaskenv_example*) в root директорії.<br>
В ньому зробити:
- FLASK_APP=web.py
- FLASK_DEBUG=1
- ENVIRONMENT=development
- SECRET_KEY=<some_secret_key>

- API_COINMARCETCAP=<api_key для доступу к coinmarketcap.com>.

- EMAIL=<xxxx - email, якій буде використано для розсилки повідомлень>.
- EMAIL_PASSWORD=<xxxx - пароль до email, якій буде використано для розсилки повідомлень>.


**Є наступні перевірки.**
- коректний нам надіслано email. чи ні.
- чи є директорія та файл де зберігається інформація.
- чи порожній файл з інформацією.


### **Docker.**
- для запуску у середовищі Windows, використовувати вайл - *"Dockerfile_win"*.<br>
Команди:
    - *"docker build -t btc -f Dockerfile_win ."*
    - *"docker run -d -p 5000:5000 btc"*<br>
- для запуску у середовищі Linux, використовувати вайл - *"Ddocker-compose.yml"*



