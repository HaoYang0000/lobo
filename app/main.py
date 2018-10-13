from __future__ import absolute_import
import os
import sys
import logging
from flask import Flask
import coloredlogs
from libs.logger_capture import LoggerCapture
import xconfig


def create_app(env=None):
    app = Flask(__name__, static_url_path='/static')
    app._static_folder = os.path.join(
        os.path.dirname(__file__),
        'static'
    )

    config = xconfig.get_config(env)
    app.config.update(**config.__dict__)

    logger = logging.getLogger()
    logger.setLevel(config.log_level)
    coloredlogs.install(
        level='DEBUG',
        fmt='%(asctime)s.%(msecs)03d %(hostname)s [%(process)d] %(name)8s %(levelname)7s %(message)s'
    )
    sys.stdout = LoggerCapture(logger.debug)

    from app.views import index

    app.register_blueprint(index.app)

    if app.debug:
        logger.info("{app} initialized".format(app=xconfig.APP_NAME))

    return app
