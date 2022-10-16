import socket

def connect(ip_address,host):
    try:
        client = socket.socket()
        client.connect((ip_address,host))
        print(client.connect_ex((ip_address,host)))
        if client.connect_ex((ip_address,host)) != 0:
            print("socket is connected")
        return 'connected'
    except Exception as e:
        print("connection id failed:",e)
        return "failed"

#connect(socket.gethostbyname(socket.gethostname()),9999)
"""
client = socket.socket()
client.connect((socket.gethostbyname(socket.gethostname()),9999))
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

"""
    input1 = input("Enter[]:")
    send1 = send1 +1
    client.send(bytes(input1, 'utf-8'))
    client.send(bytes(str(send1), 'utf-8'))
    """