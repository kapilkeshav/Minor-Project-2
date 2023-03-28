import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',1002))

file = open("main.jpg","rb")
img_data = file.read(2048)

while img_data:
    client.send(img_data)
    img_data = file.read(2048)

file.close()
client.close()