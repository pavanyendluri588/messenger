import socket

client = socket.socket()
client.connect(('172.17.0.4',5000))
#socket.gethostbyname(socket.gethostname()
print("connected\n")
name1=str(input("Enter your name:"))
client.send(bytes(name1,'utf-8'))
print(client.recv(1024).decode())
send1=0
#client.send(bytes(str(send1), 'utf-8'))
while True:
    input1 = input("Enter[]:")
    client.send(bytes(input1, 'utf-8'))
    send1 = send1 + 1
    print("send1:", send1)
   # client.send(bytes(str(send1), 'utf-8'))

    #client.send(bytes(str(send1), 'utf-8'))

    """
    input1 = input("Enter[]:")
    send1 = send1 +1
    client.send(bytes(input1, 'utf-8'))
    client.send(bytes(str(send1), 'utf-8'))
    """

