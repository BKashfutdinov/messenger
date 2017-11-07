# Функции сервера:
# принимает сообщение клиента;
# формирует ответ клиенту;
# отправляет ответ клиенту;
# имеет параметры командной строки:
# -p <port> - TCP-порт для работы (по умолчанию использует порт 7777);
# -a <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).

from socket import socket, AF_INET, SOCK_STREAM
import time
#import json
import log_config


s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind(('localhost', 8888))  # Присваивает порт 8888
s.listen(5)  # Переходит в режим ожидания запросов;
# одновременно обслуживает не более
# 5 запросов.
while True:
    client, addr = s.accept()  # Принять запрос на соединение
    print("Получен запрос на соединение от %s" % str(addr))
    timestr = time.ctime(time.time()) + "\n"

    # наоборот
    bmsg=client.recv(1024)
    jmsg = bmsg.decode('ascii')
    
    #msg = json.loads(jmsg)
    print(jmsg)

    # Обратите внимание, дальнейшая работа ведётся с сокетом клиента
    client.send(timestr.encode('ascii'))  # <- По сети должны передаваться байты,
    # поэтому выполняется кодирование строки
    client.close()

