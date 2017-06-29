import logging
import logging.config
import yaml
import os

class NinjaLogger(object):
    with open("./loggers/logging.yaml", 'rt') as f:
        config = yaml.safe_load(f.read())

    logging.config.dictConfig(config)
    instance = logging.getLogger('ninja')
