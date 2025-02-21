import json
import random
import  socket
import sys
import time 

BUFFER_SIZE = 1024
QUESTION_JSON = 'question.json'
host = "127.0.0.1"
port = 5004





def questions():
    try:
        with open(QUESTION_JSON,'r') as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(f"Something wrong with the file {e}") 
        sys.exit(1)

    except json.JSONDecodeError:
        print(f'Error:{QUESTION_JSON} is not a valid json file')   

    except Exception as e:
        print(f"Something wrong with Json File: {e}")        
        sys.exit(1)     

    
    if not isinstance(data,list) or len(data)==0:
        print("Error: Question file is empty or not in list format")
        sys.exit(1)
    return data    
    
   
    

    
    
         


def start_quiz(client_socket,questions):
    #  Send questions to the client and handle their responses. 
    for quesiton_data in questions:
        choices_index = [f"{i+1}. {choice}" for i, choice in enumerate(quesiton_data['choices'])]


        data = json.dumps({'question': quesiton_data['question'] , 'choices': choices_index, 'correct_answer': quesiton_data['answer'] })

        client_socket.sendall(data.encode('utf-8'))

        client_response = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        print(f"CLient answered {client_response}")

        try:
            choices_index = int(client_response) - 1
            if 0 <= client_response < len(quesiton_data['choices']):
                #retrieve the chosen answer. retriece the actual answer text corresponding to the chosen text
                chosen_answer = quesiton_data['choices'][choices_index]
                print(f"User Chosen answer: {chosen_answer}")

                if chosen_answer == quesiton_data['answer']:
                    print("Correct answer")
                    client_socket.sendall("Correct!".encode('utf-8'))
                else:
                    print(f"Incorrect Answer")
                    client_socket.sendall(f"Incorrect!! The correct answer is {quesiton_data['answer']}".encode('utf-8'))


            else:
                print("Invalid choice of index from client. ")
                client_socket.sendall("Invalid Choice!!".encode('utf-8'))
        except ValueError:
                print("Invalid choice index from the client") 
                client_socket.sendall("Invalid response!! Please send a number".encode('utf-8'))


                pass    
        

    

    


    
    pass


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



            #send Invitation to client
            client_socket.send(f'Do you  want to play Travia Quiz Game client {a} ?'.encode('utf-8'))

            #Recieve the response  from that  client
            response = client_socket.recv(BUFFER_SIZE).decode('utf-8').strip()

            if response == 'y':
                print("Client accepted the invitation and wants to play the quizz game!!")
                questions = questions()
                random.shuffle(questions)
                start_quiz(client_socket, questions[:5])
            else:
                print("Client decliend the invitation")
                client_socket.sendall("Goodbye!".encode('utf-8'))
                client_socket.close()    


            data = client_socket.recv(BUFFER_SIZE)
            print(F"{data.decode('utf-8')}")
            

    except socket.error as err:
        print(f"Socket error: {err}")
        sys.exit(1)

        

if __name__=="__main__":
    start_server()











