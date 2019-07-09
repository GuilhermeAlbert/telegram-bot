# Telegram BOT

Small project to improve skills using Python. Telegram BOT is a project of a Telegram Chatbot for understanding HTTP statuses using the HTTP CATS API.

See more: https://github.com/GuilhermeAlbert/telegram-bot

# Technologies used

Python 3, Telegram API, HTTP Cats API, HTTP Dogs API.

# Initial information

I follow the Mauro de Carvalho's tutorial on Medium: https://medium.com/@mdcg.dev/desenvolvendo-o-seu-primeiro-chatbot-no-telegram-com-python-a9ad787bdf6

# Important links

It is possible to use the cat or dog status API:

HTTP Status Dogs: https://httpstatusdogs.com/

HTTP Status Cats: https://http.cat

The Telegram API is: https://core.telegram.org/bots/api

# Project Commands

Command handler: https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html

Message handler: https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.messagehandler.html

Ext Filters: https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.filters.html

Ext Updater: https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.updater.html

# Enviroment configuration

Use the commands to install the enviroment. First, install PIP to manage the packages:
```shell
sudo apt-get install python-pip3
```

Install the necessary dependencies for project:
```shell
pip3 install python-telegram-bot

pip3 install -U python-dotenv
```

# Project installation

Use pip to install the requirements of project:

```shell
pip3 install -r requirements.txt
```

# Runninng the project

Enter on source folder of project and execute `python3`:

```shell
cd src

python3 
```

Type `core.py` to execute the program:

```python
>>> core.py
```

# Testing the project

Search the Telegram BOT on store: `@GuilhermeAlbertBot` and type `/http HTTP_STATUS_CODE`.

Example: `/http 404`
