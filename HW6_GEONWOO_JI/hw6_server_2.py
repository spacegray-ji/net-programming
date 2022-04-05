from socket import *
from collections import deque

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

msgbox = []

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    data = deque(str(data.decode()).split(' '))
    cmd = data.popleft()
    
    if cmd == 'send':
        id = data.popleft()
        try:        
            if not globals()['id_{}'.format(id)]:
                pass
        except:
            globals()['id_{}'.format(id)] = deque()
        globals()['id_{}'.format(id)].append(" ".join(data))
        print(globals()['id_{}'.format(id)])
        resp = 'OK'
        sock.sendto(resp.encode(), addr)

    elif cmd == 'receive':
        id = data.popleft()
        try:
            resp = globals()['id_{}'.format(id)].popleft()
            print(globals()['id_{}'.format(id)])
            if not globals()['id_{}'.format(id)]:
                del globals()['id_{}'.format(id)]
                print('deleted!')
            sock.sendto(resp.encode(), addr)
        except:
            resp = 'No messages'
            print('No messages')
            sock.sendto(resp.encode(), addr)
    
    elif cmd == 'quit':
        break

    else:
        resp = 'Wrong command'
        sock.sendto(resp.encode(), addr)
    