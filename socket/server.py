import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#has two arguments 1 is type of network ipv4 or ipv6 & 2ns one is tcp or udp by default tcp
print("socket is created")
server.bind((socket.gethostbyname(socket.gethostname()),9999))#object is passed because only one argument
#ip address range 0-->65535

server.listen(3)#only maintain 3 connections at single time
print("waiting for the connection")
c, address = server.accept()  # this will accept the request from the client side
print("connected with address:", address)
#for i in range(10):
while True:
    #c,address=server.accept()#this will accept the request from the client side
    #print("connected with address:",address)
    #c.send(bytes("welcone to feature ceos",'utf-8'))
    input1=input("Enter[]:")
    c.send(bytes(input1,'utf-8'))
c.close()#closing the client connection