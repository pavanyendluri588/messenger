import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket.gethostbyname(socket.gethostname():",socket.gethostbyname(socket.gethostname()))
client.connect((socket.gethostbyname(socket.gethostname()),9999))
print("connect to server")#'www.google.com'
while True:
     print(client.recv(1024).decode())#1024 is the max nno of bytes to recive
#print(client.recv(1024).decode())