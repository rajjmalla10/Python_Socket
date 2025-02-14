import socket
import sys 

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to Create a socket")
    print(f"Reason: {str(err)}")
    sys.exit()
print("Socket Created")

server_socket.bind(('127.0.0.1', 12345))

try:
    n = int(input("Enter number of listen backlog: "))
    if n<0:
        raise ValueError("Backlog must be a non negative integer")
    
    server_socket.listen(n)
    print(f"Server is listening with backlog size: {n}")
    
except ValueError as e:
    print("Invalid Number!!: {e}")
except socket.error as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"Unexpected error occured!: {e}")
   
while True:
            print("Server accepting connection!!")
            client_socket,addr = server_socket.accept()                
            print(f"Client Address: {addr}")
            
            while True:
                
                data = client_socket.recv(1024)
                if not data :
                    break
                
                try:
                    decode_data = data.decode('utf-8')
                    if decode_data:
                        print(f"Recieved from client :{decode_data}")
                    else:
                        break
                    
                except UnicodeDecodeError as e:
                    print(f"Error decoding data: {e}")
                    break
                
                try:
                    resposne = "Hey Client!!"
                    client_socket.send(resposne.encode('utf-8'))
                except socket.error as e:
                    print(f"Error sending response: {e}")
                    break
            
            client_socket.close()  
                        
                    
                        
                
           
            

  
    
        