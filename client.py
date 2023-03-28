import socket
H_SIZE = 10 #Header Size
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

while True:

    full=''
    new=True
    while True:
        msg = s.recv(8)
        if new:
            print(f"New message length: {msg[:H_SIZE]}")
            msglen=int(msg[:H_SIZE])
            new=False
        
        full += msg.decode("utf-8")
        if len(full)-H_SIZE == msglen:
            print("Full message recieved")
            print(full[H_SIZE:])
            new=True
            full=''

    print(full)
