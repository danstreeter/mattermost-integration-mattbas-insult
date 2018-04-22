#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from mattermost_insult.app import app
from mattermost_insult.settings import *


if __name__ == "__main__":
    if not MATTERMOST_INSULT_TOKEN:
        print("MATTERMOST_INSULT_TOKEN must be configured. Please see README.md for instructions")
        sys.exit()

    port = os.environ.get('MATTERMOST_INSULT_PORT', None) or os.environ.get('PORT', 5000)
    host = os.environ.get('MATTERMOST_INSULT_HOST', None) or os.environ.get('HOST', '0.0.0.0')
    app.run(host=str(host), port=int(port))
