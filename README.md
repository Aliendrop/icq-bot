# ICQ Bot based on [icq-bot/python-icq-bot](https://github.com/icq-bot/python-icq-bot)
## Setup
Install Python 3.6.1 and dependencies
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
## Register
- Start conversation with ***megabot*** UIN ***70001***
- /start
- /newbot - create new bot
- /setjoingroups - allow bot to join chats (set **true**)

## Run
### sender.py send message to target user, group or channel
```
python sender.py message --uin=123123123 --text='Test with link\n\nya.ru'
python sender.py message 123123123 'Test\nmessage\nwith link\n\nya.ru'
```
```
python sender.py test --uin=123123123 --text='Test message'
python sender.py test 123123123 'Test message'
```
### echo.py (runs in background) send to admin user message with target user UIN or chat ID 
```
python echo.py
```
To run the script as a windows service, use [NSSM](https://nssm.cc/)
### config.json
Contains token, name, version for echo and sender bot, admin user UIN for sender
### Target user UIN or chat ID format
- Mail.Agent: temp@mail.ru
- ICQ UIN: 123123123
- Group or Channel: 123123123@chat.agent