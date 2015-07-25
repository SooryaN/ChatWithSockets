import socket
import sys
from thread import start_new_thread
 
HOST = 'localhost'  
PORT = 8888 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
def clientthread(conn,name):
    conn.send('hello '+name+', Welcome to chatland?') 
    while True:
        data = conn.recv(1024)
        print name,':',data[:-1]
        if not data: 
            break
     
        conn.sendall(raw_input()+'\n')
     
    conn.close()
 
while 1:
    conn, addr = s.accept()
    
    data = conn.recv(1024)
    name={}
    name=data
    print name
    print 'Connected with '+ name;
    start_new_thread(clientthread ,(conn,name))
 
s.close()
