import  socket 

BUFFER_SIZE = 1024

host = "127.0.0.1"
port = 5004


try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Could not create a socket")
    print(f"Reason: {err}")
    
server_socket.bind((host,port))

server_socket.listen(2)

client_socket, addr = server_socket.accept()
