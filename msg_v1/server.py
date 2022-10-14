import socket

server = socket.socket()
server.bind((socket.gethostbyname(socket.gethostname()),9999))
print("socket is created")
status=None
users=["root"]
username="root"
server.listen(3)
c1,address1 = server.accept()
print("client1 is connected")
users.append(c1.recv(1024).decode())
c1.send(bytes("hi client1","utf-8"))
print("massage sent to client 1")
c1_send1=0
"""
while int(c1.recv(1024).decode()) == c1_send1+1:
    print(users[1],">",c1.recv(1024).decode())
    c1_send1 = c1_send1+1

"""



c2,address2 = server.accept()
print("client2 is connected")
users.append(c2.recv(1024).decode())
c2.send(bytes("hi client2","utf-8"))
print("massage sent to client 2")
c2_send1=0
"""
while int(c2.recv(1024).decode()) == c2_send1+1:
    print(users[2],">",c2.recv(1024).decode())
    c2_send1 = c2_send1+1
"""

print("users:",users)

while True:
    #if int(c1.recv(1024).decode()) == c1_send1+1:
         print(users[1],">",c1.recv(1024).decode())
         #c1_send1 = c1_send1+1

    #if int(c2.recv(1024).decode()) == c2_send1+1:
         print(users[2],">",c2.recv(1024).decode())
          #c2_send1 = c2_send1+1


