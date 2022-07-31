import yaml
import importlib

def Net(db, sock, conn, status, conn_block):
    if status == 'init':
        conn.send('sendreq'.encode())
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
    if req == 'find_key':
        key = conn.recv(2048)
        key = key.decode()
        result = db.find_key(key)
        conn.send(result.encode())
    if req == 'find_value':
        value = conn.recv(2048)
        value = value.decode()
        result = db.find_value(value)
        conn.send(result.encode())
    if req == 'list':
        listing = db.list()
        listing = str(listing)
        conn.send(listing.encode())
    try:
        with open('plugins.yml', 'r') as stream:
            out = yaml.safe_load(stream)
            plugins = out['plugins']
            for plugin in plugins:
                module = importlib.import_module(plugin)
                module.handler(db, conn, req)
    except FileNotFoundError:
        pass
    try:
        conn_block.release()
    except RuntimeError:
        pass
