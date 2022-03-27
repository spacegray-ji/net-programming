import mimetypes
from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

h_msg1 = 'HTTP/1.1 200 OK\r\n'
h_msg2 = 'Context-Type: '
h_msg3 = '\r\n'
h_msg4 = 'HTTP/1.1 404 Not Found\r\n'
h_msg5 = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
h_msg6 = '<BODY>Not Found</BODY></HTML>'

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    req_info = req[0].split(' ')
    req_info = req_info[1][1:]

    if req_info == 'index.html':
        f = open('./index.html', 'r', encoding='utf-8')
        mimeType = 'text/html'
        c.send(h_msg1.encode())
        h_msg = h_msg2 + mimeType + h_msg3
        c.send(h_msg.encode())
        c.send(h_msg3.encode())
        data = f.read()
        c.send(data.encode('euc-kr'))
    
    elif req_info == 'iot.png':
        f = open('./iot.png', 'rb')
        mimeType = 'image/png'
        c.send(h_msg1.encode())
        h_msg = h_msg2 + mimeType + h_msg3
        c.send(h_msg.encode())
        c.send(h_msg3.encode())
        data = f.read()
        c.send(data)
    
    elif req_info == 'favicon.ico':
        f = open('./favicon.ico', 'rb')
        mimeType = 'image/x-icon'
        c.send(h_msg1.encode())
        h_msg = h_msg2 + mimeType + h_msg3
        c.send(h_msg.encode())
        c.send(h_msg3.encode())
        data = f.read()
        c.send(data)

    else:
        c.send(h_msg4.encode())
        c.send(h_msg3.encode())
        c.send(h_msg5.encode())
        c.send(h_msg6.encode())
    
    c.close()