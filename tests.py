import sys
from app.utils import log
from pyrogram import Client, InputPhoneContact
from pyrogram.api import functions

tgclient = Client("telegram", config_file='conf/config.ini')
tgclient.start()

#contact = InputPhoneContact("+79281519792", "Roman", "Anikeev")
#result = tgclient.send(functions.contacts.ImportContacts([contact]))
#print('ImportContacts: {}'.format(result))
#print('{}'.format(tgclient.get_contacts()))

tgclient.stop()
