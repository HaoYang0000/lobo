import libs.config
import logging

APP_NAME = "py36-skeleton"
APP_CONFIG_FOLDER = "skeleton"


class Config(object):
    def __init__(self):
        self.ENV = 'dev'
        self.DEBUG = True
        self.log_level = logging.DEBUG


class TestingConfig(Config):
    """ prod config """
    def __init__(self):
        super(TestingConfig, self).__init__()
        self.ENV = 'dev'
        self.DEBUG = False
        self.log_level = logging.ERROR


class ProductionConfig(Config):
    """ prod config """
    def __init__(self):
        super(ProductionConfig, self).__init__()
        self.ENV = 'prod'
        self.DEBUG = False
        self.log_level = logging.ERROR


config = {
    'default': Config,
    'dev': Config,
    'testing': TestingConfig,
    'prod': ProductionConfig
}


def get_config(env=None):
    """ convenience function to get config.
    allows for complex env determination
    """
    env_config = env or libs.config.get('env', folder='')['env']

    try:
        return config[env_config]()
    except KeyError:
        return config['default']()
