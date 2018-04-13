import socket
import datetime
#function to print the current time of Client1
def getCurrentTime():
    currenttime = datetime.datetime.now()
    print("Current Time of Client1 is")
    print(currenttime)
    #updating Client1's time by adding 20 minutes
    appendedTime = currenttime + datetime.timedelta(minutes= 20)
    print("Updated Time of Client1 is")
    print(appendedTime)
    return appendedTime

host = socket.gethostname()
#port number of client 1
port = 6001
#socket using TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
appendtime = getCurrentTime()
s.sendall(appendtime.strftime("%Y%m%d%H%M%S").encode())
#receiving the average time from server
data = s.recv(1024).decode()
s.close()
print(data)
print("Time after Synchronization with Time Daemon")
print(datetime.datetime.now() + datetime.timedelta(seconds = float(data)))
