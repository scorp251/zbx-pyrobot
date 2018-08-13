from pyrogram import Client, MessageHandler
from app.utils import log, msglog
from app.config import config

if config['proxy']['enabled'] == 'True':
    proxy_host = config['proxy']['hostname']
    proxy_port = config['proxy']['port']
    proxy_user = config['proxy']['username']
    proxy_pass = config['proxy']['password']

    log.info('Initializing conection to telegram with proxy {}'.format(tuple((proxy_host, proxy_port, True, proxy_user, proxy_pass))))
    client = Client('telegram', config_file='conf/config.ini')
else:
    log.info('Initializing conection to telegram')
    client = Client('telegram', api_id, api_hash, update_workers=True, spawn_read_thread=True)

log.info('Connecting to telegram')

try:
    client.start()
except Exception as e:
    log.critical('Failed connect to telegram {}'.format(e))
    raise SystemExit


def eventHandlerCallback(client, message):
    print('Event!\n')
    msglog.debug('{}'.format(message))
#    if isinstance(update, UpdateShortMessage) and not update.out:
#        user = client(GetUsersRequest([InputUser(update.user_id, 0)]))
#        msglog.debug('{}'.format(user[0]))
#        msglog.info('Recieved message from {}_{} ({}) user_id={}: {}'.format(user[0].first_name, user[0].last_name, user[0].phone, update.user_id, update.message))
#        client(ReadHistoryRequest(InputUser(update.user_id, 0), update.id))
#        client.send_message(PeerUser(update.user_id), update.message[::-1])

client.add_handler(MessageHandler(eventHandlerCallback))
