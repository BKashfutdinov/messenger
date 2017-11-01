# Функционал.
# Первая часть домашнего задания будет заключаться в реализации простого клиент-серверного взаимодействия по протоколу JIM (JSON instant messaging):
# клиент отправляет запрос серверу;
# сервер отвечает соответствующим кодом результата.
# Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
# Функции клиента:
# сформировать presence-сообщение;
# отправить сообщение серверу;
# получить ответ сервера;
# разобрать сообщение сервера;
# параметры командной строки скрипта client.py <addr> [<port>]:
# addr - ip-адрес сервера;
# port - tcp-порт на сервере, по умолчанию 7777.

import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создать сокет TCP
s.connect(('localhost', 8888))   # Соединиться с сервером

def form_precense_msg():
    msg= {'action': 'presence'}
    # 'time': timestr
    # 'type': 'status', 
    # 'user': { 
    #     'account_name': 'C0deMaver1ck', 
    #     'status': 'Yep, I am here!'
    # } 
    # }
    jmsg = json.dumps(msg)
    #print(jmsg)
    bmsg = jmsg.encode('ascii')
    #print(bmsg)



    return bmsg

s.send(form_precense_msg())

tm = s.recv(1024)                # Принять не более 1024 байтов данных
s.close()

print("Текущее время: %s" % tm.decode('ascii'))

