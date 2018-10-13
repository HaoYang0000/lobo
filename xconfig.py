import libs.config
import logging


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


def get_config():
    return config['default']()
