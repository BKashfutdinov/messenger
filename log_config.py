"""
Создание именованного логгера.
Сообщения лога должны иметь следующий формат:
"<дата-время> <уровеньважности> <имямодуля> <имя_функции> <сообщение>"
Журналирование должно производиться в лог-файл.
На стороне сервера необходимо настроить ежедневную ротацию лог-файлов
"""
import logging

class Log():
    def __init__(self, name=False):
        self.name=name

    # Магический метод __call__ позволяет обращаться к объекту класса, как к функции
    def __call__(self, func):
        def decorated(*args, **kwargs):
            res = func(*args, **kwargs)

            print('log2: {}({}, {}) = {}'.format(func.__name__, args, kwargs, res))
            return res

        return decorated


# create formatter and add it to the handlers
def create_logger_to_server():
    # handle = logging.handlers.TimedRotatingFileHandler(filename="server.log",when='h',interval=1, backupCount=72)
    # handle.setLevel(logging.INFO)

    fmt = logging.Formatter(
        fmt="'datefmt='%Y-%m-%d %H:%M:%S' [%(levelname)s]   %(message)s'")
    # handle.setFormatter(fmt)
    logger = logging.getLogger()
    # logger.addHandler(handle)
    logger.setLevel(logging.DEBUG)
    print("logger is created")
    # logger.setLevel(logging.INFO)
    #  logger.propagate = False
    return logger


# create_logger_to_server()

logging.basicConfig(filename="log_date.log",
    format=" %(asctime)s %(levelname)s %(filename)s [line:%(lineno)d] %(message)s",
    level = logging.INFO)

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
logging.warning(u'This is a warning')

# fh = logging.FileHandler('spam.log')
# fh.setLevel(logging.DEBUG)
#
# # "<дата-время> <уровень_важности> <имя_модуля> <имя_функции> <сообщение>"
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module_name)s - %(func_name)s- %(message)s')
# fh.setFormatter(formatter)
# # add the handlers to the logger
# logger.addHandler(fh)
