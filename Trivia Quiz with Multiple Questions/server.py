import json
import random
import  socket
import sys 

BUFFER_SIZE = 1024
question_json = 'question.json'
host = "127.0.0.1"
port = 5004


def main(question_json):
    print("Welcome to the Trivia Quizz program")
    ques = input("\nWould You like to play?if yes enter: (y) if not then (n)").lower()
    while ques not in ['n','y']:
        if ques == "":
            print("No Input provided, so Quit")
            break
        ques = input("Please enter a valid input either 'y' or 'n'").lower()
    
    if ques == "y":
        start_quiz = start_quiz(client_socket)
    else:
        print("Existing the question section!")
        return            
        
        
    pass

def start_quiz(client_socket):
    

def questions(client_socket,question_json):
    data = json.loads(question_json)   
    try:
        if isinstance(data,list):
            random_item = random.choice(data)
            data.remove(random_item)
            
        else:
            print("The data is not a valid list or it's empty")
            sys.exit(1)    
            
    except Exception as e:
        print(f"Something wrong with Json File: {e}")        
        sys.exit(1)
    
    return random_item       



try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Could not create a socket")
    print(f"Reason: {err}")
    sys.exit(1)
    
server_socket.bind((host,port))

server_socket.listen(2)

try:
    print("Server accepting connection!!")
    client_socket, addr = server_socket.accept()
except socket.error as e:
    print(f"Invalid address: {e}") 
    sys.exit(1)
    
data = client_socket.recv(BUFFER_SIZE)
print(F"{data.decode('utf-8')}")










