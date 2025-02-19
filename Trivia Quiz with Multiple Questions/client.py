import socket 

host = "127.0.0.1"
port = 5003

try: 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Could not create client socket") 
    print(f"Reason: {err}")  


try:    
    client_socket.connect((host,port))
    print("Connection Request send to the server")
except ValueError as e:
    print(f"Invalid input: {e}")         
    
mesage_1 = "Connect to the server"
client_socket.send(mesage_1.encode('utf-8'))    