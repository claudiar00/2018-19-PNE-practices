import socket

# SERVER IP, PORT
IP = "127.0.0.1"
PORT = 8099



while True:

    # Before connecting to the server, we must ask the user for the string
    send_info = ''
    msg = str(input(" > "))
    while len(msg) > 0:
        send_info = send_info + msg + '\n'
        msg = str(input(''))

    if len(send_info) == 0:
        send_info = '\n'

    # Now we can create the socket and connect to the servewr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(send_info))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()