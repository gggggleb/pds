import socket
import random
import string
import sys
from pds.db import Pds_db


def test():
    status = 0

    main = Pds_db()

    def randomword(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    one = randomword(555)
    two = randomword(555)
    main.set(one, two)

    if main.get(one) == two:
        print('test set_get ok!')
        status += 1
    else:
        print('test set_get no!')
        sys.exit(1)

    one_ren = randomword(555)
    main.rename(one, one_ren)

    if main.get(one_ren) == two:
        print('test rename ok!')
        status += 1
        main.clear()
    else:
        print('test rename no!')
        sys.exit(1)

    one = randomword(555)
    two = randomword(555)
    two1 = randomword(555)
    two_plus = two + two1
    main.set(one, two)
    main.plus(one, two1)

    if main.get(one) == two_plus:
        status += 1
        print('plus test ok!')
        main.clear()
    else:
        sys.exit(1)

    one = randomword(555)
    two = randomword(555)
    main.set(one, two)

    if main.get(one) == two:
        main.rm(one)
        if main.get(one) == 'Key Error':
            status += 1
            print('rm test ok!')
        else:
            print('rm test no!')

    if status == 4:
        print('All metods OK!')
        sys.exit(0)
    else:
        print('Unit ERROR!')
        sys.exit(1)


try:
    tests = sys.argv[1]
    if tests == 'test':
        test()
except IndexError:
    pass

print('PDS is open source based on pcsd software publiched license GNU GPL3')

try:
    from config import *

    ip = ip
    port = port
    config = 1
except ModuleNotFoundError:
    config = 0

try:
    ip = sys.argv[1]
    port = int(sys.argv[2])
except IndexError:
    if config == 0:
        print('Argv not found use default')
        ip = '127.0.0.1'
        port = 4011

max_connect = 10

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))
sock.listen(max_connect)

print('Binded', ip, port)

db = Pds_db()

while True:
    conn, addr = sock.accept()
    print('Connnected', addr)
    req = conn.recv(2048)
    req = req.decode()
    print(req)

    if req == 'set':
        key = conn.recv(2048)
        value = conn.recv(2048)
        key = key.decode()
        value = value.decode()
        result = db.set(key, value)
        if result == 'Key Error':
            print('Key Error')

    if req == 'get':
        key = conn.recv(2048)
        key = key.decode()
        result = db.get(key)
        if result == 'Key Error':
            print('Key Error')
        conn.send(result.encode())

    if req == 'exit':
        sock.close()
        exit()
    if req == 'clear':
        db.clear()
    if req == 'ping':
        conn.send('PONG!'.encode())
    if req == 'rm':
        key = conn.recv(2048)
        key = key.decode()
        db.rm(key)
    if req == 'plus':
        key = conn.recv(2048)
        key = key.decode()
        value_plus = conn.recv(2048)
        value_plus = value_plus.decode()
        result = db.plus(key, value_plus)
        if result == 'Key Error':
            print('Key Error')
    if req == 'rename':
        key = conn.recv(2048)
        keynew = conn.recv(2048)
        key = key.decode()
        keynew = keynew.decode()
        db.rename(key, keynew)
