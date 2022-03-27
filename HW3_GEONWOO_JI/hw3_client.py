from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 4444))

while True:
    msg = input('Calculator:')
    if msg == 'q':
        break
    s.send(msg.encode())
#    print('Received message:', s.recv(1024).decode())
    print('Received: {:.1f}'.format(float(s.recv(1024).decode())))
    
s.close()