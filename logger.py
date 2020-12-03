import logging

# Logging
def log():
    logger = logging.getLogger('tweepy')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename='./log/bot.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
