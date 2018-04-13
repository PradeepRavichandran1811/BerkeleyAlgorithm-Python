import socket
import datetime
host = ''
#server code for connection with two clients
port = 6001
port2 = 6002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host, port))
s2.bind((host,port2))
currenttime = datetime.datetime.now()
print("Current Time of Time Daemon")
print(currenttime)
print (host , port)
s.listen(1)
s2.listen(1)
conn, addr = s.accept()
conn2, addr2 = s2.accept()
print('Connected by', addr)
timeObjects = []
while True:

    try:
        data = conn.recv(1024).decode()
        data2 = conn2.recv(1024).decode()
        if not data: break
        print ("Client Says: "+(data))
        timeobj = datetime.datetime.strptime(data, "%Y%m%d%H%M%S")
        print(timeobj.second)

        if not data2: break
        print ("Client2 Says: "+data2)
        timeobj2 = datetime.datetime.strptime(data2, "%Y%m%d%H%M%S")
        print(timeobj2.second)
        server = datetime.datetime.now()
        first = (server - timeobj).total_seconds()
        second = (server - timeobj2).total_seconds()
        #calculating the average time difference
        average = (first + second )/2
        print(average)
        print("Time after Synchronization")
        print(datetime.datetime.now() + datetime.timedelta(seconds = float(average)))
        conn.sendall(str(average).encode())
        conn2.sendall(str(average).encode())
    except socket.error:
        print ("Error Occured.")
        break

conn.close()
