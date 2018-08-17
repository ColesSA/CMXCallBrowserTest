"""Opens private config values as class"""

import json
import sys

import urllib3
from urllib3.util.retry import Retry

urllib3.disable_warnings()

class Config(object):
    """Object to control and format configuration variables"""
    with open("./config.json", 'r') as stream:
        __vars = json.load(stream)

    DEBUG=__vars['DEBUG']
    LOGGING=__vars['LOGGING']
    WEB=__vars['WEB']
    CONNECTION=WEB['CONNECTION']
    DB= __vars['DB']
    ERR=__vars['ERR']
    API=__vars['API']       

    Retry.BACKOFF_MAX = CONNECTION['BACKOFF_MAX']