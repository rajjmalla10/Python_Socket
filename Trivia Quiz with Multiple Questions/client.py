import json
import socket 

host = "127.0.0.1"
port = 5004

BUFFER_SIZE = 1024

def response():
    print("Welcome to the Trivia Quizz program")
    while True:
        ques = input("\nEnter 'y' or 'n").lower()
        while ques not in ['n','y']:
            ques = input("Please enter a valid input either 'y' or 'n'").lower()
        
        if ques == ["y",'n']:
            return ques
        
        print("INvalid input must enter either y or n")
                    
        
        
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

        if not server_resp:
            print("Server Disconnected")
            break


        if server_resp.startswith('Do you'):
            try:
                user_choice = response()
                client_socket.sendall(user_choice.encode('utf-8'))

                if user_choice == 'n':
                    print("Exciting game")
                    break
                else:
                    print("Ending!")
                    break

            except ValueError  as err:
                print(f"Incorrect Input {err}")
                break


        elif "question" in server_resp:
            try:
                question_data = json.loads(server_resp)
                print(f"\n{question_data['question']}")
                for  index, choice in  enumerate(question_data['choices'], start=1):    
                    print(f'{index} - {choice}')

                user_answer =  input("Enter the number of your answer").strip()
                client_socket.sendall(user_answer.encode('utf-8')) 
            except json.JSONDecodeError:
                print("Error: Recieved invalid question data from the server")


        else:
            print(server_resp)

    client_socket.close() 


if __name__ == "__main__":
    start_client()