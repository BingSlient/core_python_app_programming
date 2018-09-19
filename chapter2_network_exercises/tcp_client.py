# This file is for tcp connection test, setting up client side configuration

import socket as soc
from time import ctime

HOST = 'localhost'
PORT = 2048
ADDR = (HOST, PORT)
BUFSIZ = 1024

tcp_cli_soc = soc.socket(family=soc.AF_INET, type=soc.SOCK_STREAM)
tcp_cli_soc.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcp_cli_soc.send(data)
    data = tcp_cli_soc.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcp_cli_soc.close()