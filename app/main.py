from __future__ import absolute_import
import os
import sys
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import coloredlogs
from flask_apispec import FlaskApiSpec
from libs.logger_capture import LoggerCapture
from libs import config as afnconfig
import xconfig
from flask_cors import CORS

db = SQLAlchemy()
def create_app(env=None, start_response=None):
    app = Flask(__name__, static_url_path='/static')
    app._static_folder = os.path.join(
        os.path.dirname(__file__),
        'static'
    )
    app.template_folder = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}" \
                           f"/lobo-angular/dist/"

    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    config = xconfig.get_config()
    app.config.update(**config.__dict__)

    app.config['SQLALCHEMY_DATABASE_URI'] = _create_db_string(afnconfig.get('db'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    logger = logging.getLogger()
    logger.setLevel(config.log_level)
    coloredlogs.install(
        level='DEBUG',
        fmt='%(asctime)s.%(msecs)03d %(hostname)s [%(process)d] %(name)8s %(levelname)7s %(message)s'
    )
    sys.stdout = LoggerCapture(logger.debug)

    from app.views import index
    from app.views import users
    from app.views import auth

    app.register_blueprint(index.app)
    app.register_blueprint(users.app)
    app.register_blueprint(auth.app)

    # docs = FlaskApiSpec()

    db.init_app(app)

    # docs.register(
    #     users.UserResourceList, endpoint='users.UserResourceList'
    # )
    # docs.register(
    #     users.UserResourceDetail, endpoint='users.UserResourceDetail'
    # )

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
