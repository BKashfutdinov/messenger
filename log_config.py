# create formatter and add it to the handlers
import logging

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

# "<дата-время> <уровень_важности> <имя_модуля> <имя_функции> <сообщение>"
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module_name)s - %(func_name)s- %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
