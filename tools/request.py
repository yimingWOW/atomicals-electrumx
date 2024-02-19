import socket
import json
from time import sleep

port = 50001
host = 'localhost'

content = {
    "method": "blockchain.transaction.get",
    "params": ["af6df685465a42b753bf72dfdf36c43ea3c2931025411940609da6f2404b00c4", True],
    "id": 0
}

def electrumx(host, port, content):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(json.dumps(content).encode('utf-8')+b'\n')
    sleep(0.5)
    sock.shutdown(socket.SHUT_WR)
    res = ""
    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()
    print(res)
    sock.close()

electrumx(host, port, content)