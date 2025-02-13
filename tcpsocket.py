from socket import * 

import socket
import sys

try:
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to create a socket")
    print(f"Reason: {str(err)}")
    sys.exit()    
    
print("Socket Created") 


#Binding socket to an address
target_host = input("Enter the target_host name to connect: ")
target_port = input("Enter the target port: ")

try:
    socket_server.connect((target_host,int(target_port)))
    print(f"Socket Connected!! To Target Host : {target_host}, Target Port = {target_port} ")
    socket_server.shutdown(2)
except socket.error as err:
    print(f"Failed to Connect: {target_host}, {target_port}")
    print(f"Reason: {str(err)}")
    sys.exit()
        
    
    
    