import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

name  = 'Geonwoo Ji'
name = name.encode()
sock.send(name)

id = sock.recv(1024)
id = int.from_bytes(id, 'big')
print(id)

sock.close()