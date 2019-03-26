import socket
from threading import Thread
from SocketServer import ThreadingMixIn
import time
import datetime

UDP_IP = 'localhost'
UDP_PORT = 9000
BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print " Thread baru untuk "+ip+":"+str(port)

    def run(self):
        filename='testpic.jpeg'
        f = open(filename,'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((UDP_IP, UDP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print "Menunggu koneksi..."
    (conn, (ip,port)) = tcpsock.accept()
    print 'Mendapatkan koneksi dari ', (ip,port)
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()