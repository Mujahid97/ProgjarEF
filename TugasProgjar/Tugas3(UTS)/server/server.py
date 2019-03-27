import socket
import time
import os
import sys
 

def checkArg():
    if len(sys.argv) != 2:
        print('cara run program : python3 server.py [port]')
        print('contoh : python3 server.py 9000')
        sys.exit()

def checkPort():
    if int(sys.argv[1]) <= 5000:
        print("Pastikan menggunakan port diatas 5000")
        sys.exit()
    else:
        print("Port number accepted!")

def ServerExit():

    print("System will gracefully exit! Not sending any message to Client. Closing my socket!")
    s.close()
    sys.exit()


def ServerGet(g):
    print("Sending Acknowledgment of command.")
    msg = "Valid Get command. Let's go ahead "
    msgEn = msg.encode('utf-8')
    s.sendto(msgEn, clientAddr)
    print("Message Sent to Client.")

    print("In Server, Get function")

    if os.path.isfile(g):
        msg = "File exists. Let's go ahead "
        msgEn = msg.encode('utf-8')
        s.sendto(msgEn, clientAddr)
        print("Message about file existence sent.")

        c = 0
        sizeS = os.stat(g)
        sizeSS = sizeS.st_size
        print("File size in bytes:" + str(sizeSS))
        NumS = int(sizeSS / 4096)
        NumS = NumS + 1
        tillSS = str(NumS)
        tillSSS = tillSS.encode('utf8')
        s.sendto(tillSSS, clientAddr)

        check = int(NumS)
        GetRunS = open(g, "rb")
        while check != 0:
            RunS = GetRunS.read(4096)
            s.sendto(RunS, clientAddr)
            c += 1
            check -= 1
            print("Packet number:" + str(c))
            print("Data sending in process:")
        GetRunS.close()
        print("Sent from Server - Get function")

    else:
        msg = "Error: File tidak ada dalam direktori server."
        msgEn = msg.encode('utf-8')
        s.sendto(msgEn, clientAddr)
        print("Message Sent.")


def ServerPut():
    print("Sending Acknowledgment of command.")
    msg = "Valid Put command. Let's go ahead "
    msgEn = msg.encode('utf-8')
    s.sendto(msgEn, clientAddr)
    print("Message Sent to Client.")

    print("In Server, Put function")
    if t2[0] == "put":

        BigSAgain = open(t2[1], "wb")
        d = 0
        print("Penerimaan paket data akan dimulai jika file ditemukan.")
        try:
            Count, countaddress = s.recvfrom(4096)
        except ConnectionResetError:
            print(
                "Error. Nomor port tidak sesuai.")
            sys.exit()
        except:
            print("Timeout")
            sys.exit()

        tillI = Count.decode('utf8')
        tillI = int(tillI)

        while tillI != 0:
            ServerData, serverAddr = s.recvfrom(4096)

            dataS = BigSAgain.write(ServerData)

            d += 1
            tillI = tillI - 1
            print("Received packet number:" + str(d))


        BigSAgain.close()
        print("New file closed. Check contents in your directory.")


def ServerElse():
    msg = "Error: You asked for: " + \
        t2[0] + " which is not understood by the server."
    msgEn = msg.encode('utf-8')
    s.sendto(msgEn, clientAddr)
    print("Message Sent.")


host = ""
checkArg()
try:
    port = int(sys.argv[1])
except ValueError:
    print("Error. Exiting. Nomor port tidak valid.")
    sys.exit()
except IndexError:
    print("Error. Exiting. Nomor port tidak valid.")
    sys.exit()
checkPort()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Server socket initialized")
    s.bind((host, port))
    print("Successful binding. Waiting for Client now.")

except socket.error:
    print("Failed to create socket")
    sys.exit()

while True:
    try:
        data, clientAddr = s.recvfrom(4096)
    except ConnectionResetError:
        print(
            "Error. Nomor port tidak sesuai.")
        sys.exit()
    text = data.decode('utf8')
    t2 = text.split()
    if t2[0] == "get":
        print("Go to get func")
        ServerGet(t2[1])
    elif t2[0] == "put":
        print("Go to put func")
        ServerPut()
    elif t2[0] == "exit":
        print("Go to Exit function")
        ServerExit()
    else:
        ServerElse()

print("Program will end now. ")
quit()