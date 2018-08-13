import os
from pyrogram.api import functions
from pathlib import Path
from flask import Blueprint, redirect, render_template, url_for, request, session
from app.utils import log
from app.tgclient import client

bp = Blueprint('contacts', __name__, url_prefix='/contacts', template_folder='templates', static_folder='static')

@bp.route('/')
def index():
    return redirect(url_for('.contact_list'), code=301)

@bp.route('/list')
def contact_list():
    errormsg = ''
    if 'error' in session:
        errormsg = session['error']
        session.pop('error')

    users = []

    contacts = client.send(functions.contacts.GetContacts(0))
    log.debug('{}'.format(contacts))

    for user in contacts.users:
        user_profile = dict()
        user_profile['id'] = user.id
        user_profile['access_hash'] = user.access_hash
        user_profile['first_name'] = user.first_name
        user_profile['last_name'] = user.last_name
        user_profile['phone'] = user.phone
        if user.photo:
            filename = 'app/contacts/static/tmp/{}.jpg'.format(user.photo.photo_id)
            if not Path(filename).is_file():
                log.info('Downloading profile photo {}_{} to {}'.format(user.first_name, user.last_name, filename))
                photos = client.get_user_profile_photos(user.id)
#                log.debug('photos: {}'.format(photos))
                for photo in photos:
                    log.debug('Hello')
                    if photo.width == 640:
                        user_profile['photo'] = client.download_media(photo.file_id, file_name = '{}.jpg'.format(user.photo.photo_id))
#            user_profile['photo'] = '{}.jpg'.format(user.photo.photo_id)
        users.append(user_profile)

#    locale.setlocale(locale.LC_ALL, "")

#    output = render_template('contact_list.html', contacts=sorted(users, key=lambda k: k['first_name']), errormsg=errormsg)
#    output = render_template('contact_list.html', contacts=sorted(users, key=lambda k: -int(k['first_name'].replace(",", ""))), errormsg=errormsg)
#    output = render_template('contact_list.html', contacts=users.sort(key='first_name'), errormsg=errormsg)

    output = render_template('contact_list.html', contacts=users, errormsg=errormsg)
    return output

@bp.route('/add', methods=['POST'])
def contact_add():
    log.debug('{}'.format(request.form))

@bp.route('/delete', methods=['POST'])
def contact_del():
    log.debug('{}'.format(request.form))

