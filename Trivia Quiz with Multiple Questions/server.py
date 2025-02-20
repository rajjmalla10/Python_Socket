import json
import random
import  socket
import sys 

BUFFER_SIZE = 1024
question_json = 'question.json'
host = "127.0.0.1"
port = 5004



def start_quiz(client_socket,question_json):
    question_data= questions(question_json)

    question = question_data['question']
    choices = question_data['choices']
    answer = question_data['answer']


    #send question and  choices to the client

    data = json.dumps({'question': question, 'choices': choices})
    client_socket.sendall(data.encode('utf-8'))


    
    pass




def questions(client_socket,question_json):
    try:
        with open(question_json,'r') as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(f"Something wrong with the file {e}") 
        sys.exit(1)

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


def start_server():
    try:
        # 'Start the server and handle client and server connection'
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            print("Could not create a socket")
            print(f"Reason: {err}")
            sys.exit(1)
            
        server_socket.bind((host,port))

        server_socket.listen(2)

        a = 0
        while True:
            a += 1
            try:
                print("Server accepting connection!!")
                client_socket, addr = server_socket.accept()
                print(f'Client {addr} connected')
            except socket.error as e:
                print(f"Invalid address: {e}") 
                sys.exit(1)


            response = client_socket.recv(BUFFER_SIZE).decode('utf-8')

            #send Invitation to client
            client_socket.send(f'Do you  want to play Travia Quiz Game client {a} ?'.encode('utf-8'))

            #Recieve the response  from that  client
            response = client_socket.recv(BUFFER_SIZE).decode('utf-8').strip()

            if response == 'y':
                print("Client accepted the invitation and wants to play the quizz game!!")
                start_quiz(client_socket,question_json)
            else:
                print("Client decliend the invitation")
                client_socket.close()    

            data = client_socket.recv(BUFFER_SIZE)
            print(F"{data.decode('utf-8')}")

    except socket.error as err:
        print(f"Socket error: {err}")
        sys.exit(1)

        

if __name__=="__main__":
    start_server()











