import json
import socket 

host = "127.0.0.1"
port = 5003

BUFFER_SIZE = 1024

def response():
    print("Welcome to the Trivia Quizz program")
    ques = input("\nEnter 'y' or 'n").lower()
    while ques not in ['n','y']:
        ques = input("Please enter a valid input either 'y' or 'n'").lower()
    
    if ques == "y":
        return ques
    else:
        print("Existing the question section!")
        return            
        
        
    pass



def start_client():
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
        
    while True:    
        server_resp = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        print(server_resp)

        if server_resp:
            try:
                response()
                if response()== 'y':
                    client_socket.sendall('y'.encode('utf-8'))
                elif response() == 'n':
                    client_socket.sendall('n'.encode('utf-8'))
                    break
                else:
                    print("Ending!")
                    break

            except ValueError  as err:
                print(f"Incorrect Input {err}")
                break


        elif "question" in server_resp:
            question_data = json.loads(server_resp)
            print(f"\n{question_data['question']}")
            for  index, choice in  enumerate(question_data['choices']):    
                print(f'{index} - {choice}')

            user_answer =  input("Enter the answer").strip()
            client_socket.sendall(user_answer.encode('utf-8')) 



        else:
            print(server_resp)

    client_socket.close() 


if __name__ == "__main__":
    start_client()