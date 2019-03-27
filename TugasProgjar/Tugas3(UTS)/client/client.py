import socket
import time
import os
import sys


def checkArg():
    if len(sys.argv) != 3:
        print('cara run program : python3 client.py [server_ip] [port]')
        print('contoh : python3 client.py localhost 9000')
        sys.exit()

def checkPort():
    if int(sys.argv[2]) <= 5000:
        print("Pastikan menggunakan port diatas 5000")
        sys.exit()
    else:
        print("Port number accepted!")

checkArg()
try:
    socket.gethostbyname(sys.argv[1])
except socket.error:
    print("Invalid host name")
    sys.exit()

host = sys.argv[1]
try:
    port = int(sys.argv[2])
except ValueError:
    print("Error. Nomor port tidak valid")
    sys.exit()
except IndexError:
    print("Error. Nomor port tidak valid")
    sys.exit()

checkPort()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Client socket initialized")
    s.setblocking(0)
    s.settimeout(15)
except socket.error:
    print("Failed to create socket")
    sys.exit()

while True:
    command = input(
        "Berikut ini adalah perintah yang dapat digunakan : \n1. get [file_name.extension]\n2. put [file_name.extension]\n3. exit\n ")

    CommClient = command.encode('utf-8')
    try:
        s.sendto(CommClient, (host, port))
    except ConnectionResetError:
        print(
            "Error. Nomor port tidak sesuai.")
        sys.exit()
    CL = command.split()
    print("We shall proceed, but you may want to check Server command prompt for messages, if any.")
    if CL[0] == "get":
        print("Checking for acknowledgement")
        try:
            ClientData, clientAddr = s.recvfrom(51200)
        except ConnectionResetError:
            print(
                "Error. Nomor port tidak sesuai")
            sys.exit()
        except:
            print("Timeout")
            sys.exit()
        text = ClientData.decode('utf8')
        print(text)
        print("Inside Client Get")

        try:
            ClientData2, clientAddr2 = s.recvfrom(51200)
        except ConnectionResetError:
            print(
                "Error. Nomor port tidak sesuai")
            sys.exit()
        except:
            print("Timeout")
            sys.exit()

        text2 = ClientData2.decode('utf8')
        print(text2)

        if len(text2) < 30:
            if CL[0] == "get":
                BigC = open("Received-" + CL[1], "wb")
                d = 0
                try:
                    CountC, countaddress = s.recvfrom(4096)
                except ConnectionResetError:
                    print(
                        "Error. Nomor port tidak sesuai")
                    sys.exit()
                except:
                    print("Timeout")
                    sys.exit()

                tillC = CountC.decode('utf8')
                tillCC = int(tillC)
                print("Penerimaan paket data akan dimulai jika file ditemukan.")
                while tillCC != 0:
                    ClientBData, clientbAddr = s.recvfrom(4096)
                    dataS = BigC.write(ClientBData)
                    d += 1
                    print("Received packet number:" + str(d))
                    tillCC = tillCC - 1

                BigC.close()
                print(
                    "FIle baru diterima, silahkan cek direktori.")

    elif CL[0] == "put":
        print("Checking for acknowledgement")
        try:
            ClientData, clientAddr = s.recvfrom(4096)
        except ConnectionResetError:
            print(
                "Error. Nomor port tidak sesuai")
            sys.exit()
        except:
            print("Timeout or some other error")
            sys.exit()

        text = ClientData.decode('utf8')
        print(text)
        print("We shall start sending data.")

        if text == "Valid Put command. Let's go ahead ":
            if os.path.isfile(CL[1]):

                c = 0
                size = os.stat(CL[1])
                sizeS = size.st_size
                print("File size in bytes: " + str(sizeS))
                Num = int(sizeS / 4096)
                Num = Num + 1
                print("Number of packets to be sent: " + str(Num))
                till = str(Num)
                tillC = till.encode('utf8')
                s.sendto(tillC, clientAddr)
                tillIC = int(Num)
                GetRun = open(CL[1], "rb")

                while tillIC != 0:
                    Run = GetRun.read(4096)
                    s.sendto(Run, clientAddr)
                    c += 1
                    tillIC -= 1
                    print("Packet number:" + str(c))
                    print("Data sending in process:")

                GetRun.close()

                print("Sent from Client - Put function")
            else:
                print("File tidak ditemukan.")
        else:
            print("Invalid.")

    elif CL[0] == "exit":
        print(
            "Server will exit if you have entered port number correctly, but you will not receive Server's message here.")

    else:
        try:
            ClientData, clientAddr = s.recvfrom(51200)
        except ConnectionResetError:
            print(
                "Error. Nomor port tidak sesuai")
            sys.exit()
        except:
            print("Timeout")
            sys.exit()
        text = ClientData.decode('utf8')
        print(text)

print("Program will end now. ")
quit()
