import json
import sys
import logging
import fire
from icq.bot import ICQBot


CONFIG = 'config.json'
LOG = 'sender.log'

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
    name = config_data['sender_name']
    version = config_data['sender_version']
    token = config_data['sender_token']
    return name, version, token


class ICQBotSender(object):

    def __init__(self):
        _name, _version, _token = get_settings()
        self.NAME = _name
        self.VERSION = _version
        self.TOKEN = _token
        dbg_config = f'NAME:{self.NAME}, V:{self.VERSION}, TOKEN:{self.TOKEN}'
        log.info(dbg_config)
        print(dbg_config)

    def test(self, uin, text):
        dbg_param = (
            f'{__class__.__name__}.message, '
            f'UIN:{str(uin)}, TEXT:{text}')
        log.info(dbg_param)
        print(dbg_param)

    def message(self, uin, text):
        text = str(text).replace('\\n', '\n')
        dbg_param = (
            f'{__class__.__name__}.message, '
            f'UIN:{str(uin)}, TEXT:{text}')
        log.info(dbg_param)
        print(dbg_param)

        try:
            bot = ICQBot(
                token=self.TOKEN,
                name=self.NAME,
                version=self.VERSION)
            response = bot.send_im(target=uin, message=text)
            dbg_resp = f'RESPONSE: {response}'
            log.info(dbg_resp)
            print(dbg_resp)

            sys.exit(0)
        except Exception as e:
            dbg_resp = f'RESPONSE: ERROR {e}'
            log.error(dbg_resp)
            print(dbg_resp)

            sys.exit(1)


if __name__ == '__main__':
    fire.Fire(ICQBotSender)
