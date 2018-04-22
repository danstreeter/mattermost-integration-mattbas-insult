# -*- coding: utf-8 -*-
import os

# the Mattermost token or tokens generated when you created your outgoing webhook
# multiple tokens needs to be separated by a colon
MATTERMOST_INSULT_TOKEN = os.environ.get('MATTERMOST_INSULT_TOKEN', '').split(':')
