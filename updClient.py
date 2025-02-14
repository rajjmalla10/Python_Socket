import socket
import sys 

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as err:
    print("Could not create socket")
    print(f"Reason: {err}")
    sys.exit(1)

data = "Hello Server, how are you?"
try:
    client_socket.sendto(data.encode('utf-8'),('127.0.0.1', 12345))
    print("Data send sucesfully")
except ValueError as e:
    print(f"Wrong Value!!: {e}")
except socket.error as err:
    print("Invalid Usage: {err}") 
    client_socket.close()
    sys.exit(1)   


try:
    new_data , addr = client_socket.recvfrom(4096)
    print("Recieved from the server! server says: ")
    print(new_data.decode('utf-8'))
except socket.error as err:
    print(f"Failed to recieve data: {err}")
    client_socket.close()
    sys.exit(1)    

finally:
    client_socket.close()
    print("Socket closed")    