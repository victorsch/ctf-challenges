import socket
import ast

# define the host and port to listen on
HOST = '0.0.0.0'
PORT = 48977

# create a socket object and bind it to the host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# listen for incoming connections
server_socket.listen()

# define a dictionary for the context in which eval will be run

keep_going = True
while True:
    try:
        # accept a connection
        client_socket, addr = server_socket.accept()
        balance = 1543.27
        
        print(f'Connection from {addr} has been established!')
        
        while keep_going:
            client_socket.send(str("\n").encode('utf-8'))
            client_socket.send(str("Welcome to your banking application! Please tell us what you would like to do: \n").encode('utf-8'))
            client_socket.send(str("1. Deposit\n").encode('utf-8'))
            client_socket.send(str("2. Withdraw\n").encode('utf-8'))
            client_socket.send(str("3. Balance\n").encode('utf-8'))

            # receive the data from the client
            data = client_socket.recv(1024)

            # decode the data into a string
            data_str = data.decode('utf-8')
            
            try:
                if (str(data_str.strip()) == "1"):
                    client_socket.send(str(f"How much would you like to deposit?\n").encode('utf-8'))
                    deposit_amount = client_socket.recv(1024).decode('utf-8')
                    client_socket.send(str(f"You have deposited {deposit_amount}\n").encode('utf-8'))
                    result = eval(str(f"{deposit_amount.strip()} + {balance}"))
                    balance = result
                    client_socket.send(str(f"Your new balance is: {result}\n").encode('utf-8'))
                elif (str(data_str.strip()) == "2"):
                    client_socket.send(str("How much would you like to withdraw?\n").encode('utf-8'))
                    amount = client_socket.recv(1024).decode('utf-8')
                    client_socket.send(str(f"You have withdrawn {amount}\n").encode('utf-8'))
                    result = eval(str(f"{balance} - {amount}"))
                    balance = result
                    client_socket.send(str(f"Your new balance is: {result}\n").encode('utf-8'))
                elif (str(data_str.strip()) == "3"):
                    client_socket.send(str(f"Your balance is: {balance}\n").encode('utf-8'))
                
            except BrokenPipeError:
                client_socket.close()
                keep_going = False
                break
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt detected. Closing server...")
                keep_going = False
                # close the server socket
                client_socket.close()
                break
            except Exception as e:
                client_socket.send(str(e).encode('utf-8'))
                keep_going = False
                # close the connection
                client_socket.close()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Closing server...")
        # close the server socket
        client_socket.close()
        break