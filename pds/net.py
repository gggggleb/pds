import socket
import threading
from _thread import *

from pds.handler import Net


def main(ip, port, max_connect, db):
    conn_block = threading.Lock()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(max_connect)
    while True:
        conn, addr = sock.accept()
        print('Connected!', addr)
        conn_block.acquire()
        status = conn.recv(2048)
        status = status.decode()
        start_new_thread(Net, (db, sock, conn, status, conn_block))
