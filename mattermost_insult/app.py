# -*- coding: utf-8 -*-
import logging
import json
import re

import requests
from flask import Flask
from flask import request
from flask import Response

from mattermost_insult.settings import *


logging.basicConfig(
    level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')
app = Flask(__name__)


@app.route('/')
def root():
    """
    Home handler
    """

    return "OK"


@app.route('/insult', methods=['POST'])
def insult():
    """
    Mattermost new post event handler
    """
    try:
        slash_command = False
        resp_data = {}
        resp_data['response_type'] = 'in_channel'

        data = request.form

        if 'text' in data:
            logging.error('Some text was found: {}'.format(data['text']))
            user = parseOutUser(data['text'])+" " or ''

        if not 'token' in data:
            raise Exception('Missing necessary token in the post data')

        if data['token'] not in MATTERMOST_INSULT_TOKEN:
            raise Exception('Tokens did not match, it is possible that this request came from somewhere other than Mattermost')

        resp_data['text'] = "> " + user + get_insult()

    except Exception as err:
        msg = err.message
        logging.error('Unable to insult you :: {}'.format(msg))
        resp_data['text'] = msg
    finally:
        resp = Response(content_type='application/json')
        resp.set_data(json.dumps(resp_data))
        return resp


def get_insult():
    try:
        resp = requests.get('https://insult.mattbas.org/api/insult.json')

        resp_data = resp.json();

        if resp.status_code is not requests.codes.ok:
            logging.error('Encountered error using Insult API, text=%s, status=%d, response_body=%s' % (text, resp.status_code, resp.json()))
            return None
        
        return resp_data['insult']

    except Exception as err:
        logging.error('unable to get an insult :: {}'.format(err))
        return None

def parseOutUser(text):
    try:
        p = re.compile('\@{1}[a-z0-9\.\-]*')
        m = p.match(text)
        if m:
            user = m.group()
            if user:
                return user
            return ''
        return ''
    except Exception as err:
        return ''
