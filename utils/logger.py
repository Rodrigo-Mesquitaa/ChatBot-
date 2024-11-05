import logging
from config.config import Config

def get_logger(name):
    # Configura o logger com o nível especificado em Config.LOG_LEVEL
    logger = logging.getLogger(name)
    logger.setLevel(Config.LOG_LEVEL)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    return logger
