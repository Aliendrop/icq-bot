import json
import logging
from icq.bot import ICQBot
from icq.filter import MessageFilter
from icq.handler import MessageHandler


CONFIG = 'config.json'
LOG = 'echo.log'

formatter = '%(asctime)s; %(msecs)d; %(name)s; %(levelname)s; %(message)s;'
dateformat = '%Y-%m-%d; %H:%M:%S'
logging.basicConfig(
    filename=LOG, level=logging.INFO, format=formatter, datefmt=dateformat)

# Enable logging.DEBUG for Debug ICQBot
# logging.basicConfig(filename=LOG, level=logging.DEBUG)

log = logging.getLogger(__name__)
log.info(f'RUN {__file__}')  # log.error("An error has happened!")


def get_settings():
    with open(CONFIG) as config_file:
        config_data = json.load(config_file)
    name = config_data['echo_name']
    version = config_data['echo_version']
    token = config_data['echo_token']
    admin = config_data['echo_admin']
    return name, version, token, admin


NAME, VERSION, TOKEN, ADMIN = get_settings()
dbg_config = f'NAME:{NAME}, V:{VERSION}, TOKEN:{TOKEN}, ADMIN:{ADMIN}'
log.info(dbg_config)
print(dbg_config)


def message_event(bot, event):
    usr_source = event.data["source"]["aimId"]
    usr_message = event.data["message"]

    dbg_param = (
        f'{__name__}.message_event, '
        f'UIN:{str(usr_source)}, TEXT:{usr_message}')
    log.info(dbg_param)
    print(dbg_param)

    message = f'User: {usr_source}\nMessage: {usr_message}'
    bot.send_im(target=ADMIN, message=message)


def main():
    bot = ICQBot(token=TOKEN, name=NAME, version=VERSION)
    bot.dispatcher.add_handler(
        MessageHandler(filters=MessageFilter.message, callback=message_event))
    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
