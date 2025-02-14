import os
import socket
import sys

import tqdm

host = '127.0.0.1'
port = 5001
file_directory = r"C:\Users\ACER\OneDrive\Desktop\rajmalla\321519144_139367758921686_3745951446647280889_n.jpg"

BUFFERSIZE = 4096

filename = os.path.basename(file_directory)
filesize = os.path.getsize(file_directory)

seperator = "<SEPERATOR>"
try:
    client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created sucesfully!!")
except socket.error as err:
    print("Could not create socket")
    print(f"Reason: {err}")
    sys.exit(1)
    
print(f"[+] Connecting to {host}:{port}")

try:
    client_server.connect((host,port))
    print("Connection Request Send") 
except ValueError as err:
    print("Failed to connect") 
    print(f"Reason: {err}")
    sys.exit(1)

client_server.send(f"{filename} {seperator} {filesize}".encode('utf-8'))

progress = tqdm.tqdm(range(filesize), desc=f"sending {filename}", unit='B', unit_scale=True, unit_divisor=1024)


try:
    if os.path.exists(file_directory):
        with open(file_directory, 'rb') as file:
            while True:
                data = file.read(BUFFERSIZE)
                if not data:
                    break
                client_server.sendall(data)
                progress.update(len(data))
except socket.error as e:
    print(f"Error while reading file: {e}")
except FileNotFoundError:
    print(f'The file {filename} was not found please check the file and try again.')                
except Exception as e:
    print(f"An unexpected error occured: {e}")

response = client_server.recv(1024).decode('utf-8')
print(f"server response: {response}")



client_server.close()
                
                
        
        
        
        


    
    
          







