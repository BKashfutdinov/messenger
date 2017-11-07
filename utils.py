import json
import log_config

#log=Log()

@Log("convert functions")
def convert_dict_to_bytes(msg):
    if isinstance(msg, dict):
        jmsg = json.dumps(msg)
        bmsg = jmsg.encode('ascii')
        return bmsg
    else:
        raise TypeError


def convert_bytes_to_dict(msg):
    if isinstance(msg, bytes):
        jmsg = msg.decode(ENCODING)
        dict_msg = json.loads(jmsg)
        if isinstance(dict_msg,dict):
            return dict_msg
        else:
            raise TypeError
    else:
        raise TypeError


def send_message(sock, message):
    """
    Отправка сообщения
    :param sock: сокет
    :param message: словарь сообщения
    :return: None
    """
    # Словарь переводим в байты
    bprescence = convert_dict_to_bytes(message)
    # Отправляем
    sock.send(bprescence)


def get_message(sock):
    """
    Получение сообщения
    :param sock:
    :return: словарь ответа
    """
    # Получаем байты
    bresponse = sock.recv(1024)
    # переводим байты в словарь
    response = convert_bytes_to_dict(bresponse)
    # возвращаем словарь
    return response
