import logging
from logging.handlers import SMTPHandler

from flask import Flask
from flask.logging import default_handler

from .generic.connection import SafeRequest
from .generic.scheduler import Scheduler

from .config import Config

from .url import APICall, form_url

from io import BytesIO

app = Flask(__name__)
#cors = CORS(app, resources={r"/api/*": {"origins": "*", 'methods': 'GET', 'supports_credentials': True}})

app.config.from_object(Config)

conn = SafeRequest(Config.WEB['UID'], 
                   Config.WEB['PWD'], 
                   Config.WEB['VERIFICATION'],
                   Config.CONNECTION['MAX_RETRIES'], 
                   Config.CONNECTION['BACKOFF_FACTOR'], 
                   Config.CONNECTION['STATUS_FORCELIST'])

if(Config.LOGGING):
        logger = logging.getLogger()
        logger.level = logging.DEBUG if Config.DEBUG else logging.ERROR
        logger.addHandler(default_handler)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/test')
def test():
    url = form_url(APICall.MapResources.get_floor_image, 
        "Welcome Center", 
        "Welcome Center", 
        "Welcome Center First Floor")
    return conn.get_image_from(url)