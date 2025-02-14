import os
import socket
import sys

import tqdm 

host = '0.0.0.0'
port = 5001

file_directory = "file_reciever"
BUFFERSIZE = 4096

seperator = "<SEPERATOR>"

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to create a socket")
    print(f"Reason: {err}")    
    sys.exit(1)
    
try:
    server_socket.bind((host,port))
except ValueError as e:
    print(f"Invalid valid: {e}")
    

server_socket.listen(4)

print(f"[*] Listening as {host}:{port}")

# Once the client connects to our server, we need to accept that connection:


try:
    print("Accepting the client")
    client_socket, addr = server_socket.accept()
except socket.error as err:
    print(f"Error occured while accepting connection: {err}") 
    
print(f"Client with : {addr} address  Connected") 


# Remember that when the client is connected, it'll send the name and size of the file. Let's receive them:



data_recieved = client_socket.recv(BUFFERSIZE).decode('utf-8')

filename , filesize = data_recieved.split(seperator)

filename = os.path.basename(filename)
filesize = int(filesize)

os.makedirs(file_directory,exist_ok=True)
progress = tqdm.tqdm(total=filesize, desc=f"receiving {filename}", unit='B', unit_scale=True, unit_divisor=1024)

try: 
    with open(os.path.join(file_directory,filename),'wb') as file:
        while True:
            bytes_read = client_socket.recv(BUFFERSIZE)
            if not bytes_read:
                break
            
            file.write(bytes_read)
            progress.update(len(bytes_read))
except socket.error as err:
    print(f"Invalid file handling {err}")
except FileNotFoundError as e:
    print(f"File not exist: {e}")
except Exception as e:
    print(f"Something went wrong: {e}")

print("Completed")    
client_socket.send("File Recvieved Sucesfully".encode('utf-8'))

progress.close()
client_socket.close()
server_socket.close()                        



    

    
    