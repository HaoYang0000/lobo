from __future__ import absolute_import
import os
import sys
import logging
from flask import Flask
import coloredlogs
from libs.logger_capture import LoggerCapture
from libs import config as afnconfig
import xconfig
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(env=None):
    app = Flask(__name__, static_url_path='/static')
    app._static_folder = os.path.join(
        os.path.dirname(__file__),
        'static'
    )

    config = xconfig.get_config()
    app.config.update(**config.__dict__)

    app.config['SQLALCHEMY_DATABASE_URI'] = _create_db_string(afnconfig.get('db'))

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
        logger.info("{app} initialized".format(app='lobo'))

    return app


def _create_db_string(config):
    """ Helper function for creating a MySQL URI
    """
    return (
        "mysql+pymysql://{user}:{password}@{host}:{port}/"
        "{schema}?charset=utf8mb4"
    ).format(
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port'],
        schema=config['schema']
    )
