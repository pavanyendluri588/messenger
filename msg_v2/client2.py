import socket

client = socket.socket()
client.connect((socket.gethostbyname(socket.gethostname()),9999))
print("connected\n")
name1=str(input("Enter your name:"))
client.send(bytes(name1,'utf-8'))
print(client.recv(1024).decode())
send1=1
while True:
    #client.send(bytes(str(send1), 'utf-8'))
    input1 = input("Enter[]:")
    client.send(bytes(input1, 'utf-8'))
    send1 = send1 + 1
    print("send1:",send1)
    #client.send(bytes(str(send1), 'utf-8'))