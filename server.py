import socket
while True:
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',1002))
    server.listen()

    client_socket, client_address = server.accept()

    file = open('C:/Users/91981/Desktop/Minor Project/chatroom/fin_msg.jpg',"wb")

    img_chunk = client_socket.recv(2048) #stream based protocol
    while img_chunk:
        file.write(img_chunk)
        img_chunk = client_socket.recv(2048)

    file.close()
    client_socket.close()
