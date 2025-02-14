import socket 

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Client Socket creation Failed")
    print(f"Reason: {str(err)}")
    
try:    
    client_socket.connect(('127.0.0.1',12345))
except ValueError as e:
    print("Wrong value!!: {e}")
    
     
payload = input("Enter the message to the server: ")

try:
    while True:
        client_socket.send(payload.encode('utf-8'))  
        
        data = client_socket.recv(1024)
        print(str(data))
        
        more_data = input("would You like to send more data!!: Press y if u want to send 'yes', n if you want to send 'No'").lower() 
        
        while len(more_data)!=1 or more_data not in ['y','n']:
            print("Invalid input Please enter either ['y' or 'n']")
            more_data = input("would You like to send more data!!: Press y if u want to send 'yes', n if you want to send 'No'").lower()
        
        if more_data == 'y':
            payload = input("Enter the payload(data you wnat to send)")
        else:
            break  
except KeyboardInterrupt:
    print("Inturrupted by the user!!")
client_socket.close()    
                  

        

            