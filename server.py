import socket
import time
H_SIZE = 10 #Header Size
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")
    msg = "Welcome to the server"
    msg = f'{len(msg):<{H_SIZE}}' + msg   #Fixed Length Header
    clientsocket.send(bytes(msg,"utf-8"))
    
    while True:
        time.sleep(3)
        msg='connection is still alive'
        msg = f'{len(msg):<{H_SIZE}}' + msg
        clientsocket.send(bytes(msg,"utf-8"))