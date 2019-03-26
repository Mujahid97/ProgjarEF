import socket
import threading
import time
import datetime

UDP_IP = 'localhost'
UDP_PORT = 9000
BUFFER_SIZE = 1024
num = int

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((UDP_IP, UDP_PORT))
waktu = datetime.datetime.now()
with open('client2_received_file'+ format(waktu) + '.jpeg', 'wb') as f:
    print 'file opened'
    while True:
        data = s.recv(BUFFER_SIZE)
        if not data:
            f.close()
            print 'file closed'
            break
        f.write(data)

print('Berhasil mengambil gambar')
s.close()