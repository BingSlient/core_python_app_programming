# This is file is for tcp connection test, setting up the server side configuration

import socket as soc 
from time import ctime

HOST = ''
PORT = 2048
ADDR = (HOST, PORT)
BUFSIZ = 1024

tcp_ser_soc = soc.socket(family=soc.AF_INET, type=soc.SOCK_STREAM)
tcp_ser_soc.bind(ADDR)
tcp_ser_soc.listen(5)

while True:
    print('Waiting for connection... ')
    tcp_cli_soc, addr = tcp_ser_soc.accept()
    print('... connected from:', addr)

    while True:
        data = tcp_cli_soc.recv(BUFSIZ)
        if not data:
            break
        tcp_cli_soc.send('[{}]{}'.format(ctime(), data))

    tcp_cli_soc.close()
tcp_ser_soc.close()