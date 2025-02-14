import socket
import sys 

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as err:
    print(" Failed to create a socket ")    
    print(f"Reasom: {err}")
    sys.exit()

server_socket.bind(('127.0.0.1',12345))

while True:
      data,addr = server_socket.recvfrom(1024)
      print(f"Recieved from {addr}: {data.decode('utf-8')}")
      
      
      reply = "I am server!!"
      server_socket.sendto(reply.encode('utf-8'),addr)
          
      