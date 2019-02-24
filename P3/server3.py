import socket
#import termcolor
from Seq3 import Seq

IP = "127.0.0.1"
PORT = 8099
MAX_OPEN_REQUESTS = 5
# number of users that can be connected at the same time

def validSequence(s):
    valid = 'AGCT'
    for letter in s:
        if letter not in valid:
            return False
    return True

def analyse(s1, command):

    print("Working using the comand:", command)
    if command == "len":
        return s1.len()
    elif command == "complement":
        return s1.complement().get_strbase()
    elif command == "reverse":
        return s1.reverse().get_strbase()
    elif command == "countA":
        return s1.count('A')
    elif command == "countT":
        return s1.count('T')
    elif command == "countG":
        return s1.count('G')
    elif command == "countC":
        return s1.count('C')
    elif command == "percA":
        return s1.perc("A")
    elif command == "percT":
        return s1.perc("T")
    elif command == "percG":
        return s1.perc("G")
    elif command == "percC":
        return s1.perc("C")
    else:
        return"ERROR"
def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")
    # termcolor.cprint(msg, 'magenta')#using termcolor I decided to put it magenta!!!!

    if msg == '\n':
        response = 'Still connected'
        # here we know the program is still running
    else:
        slice = msg.split('\n')
        print("Validating", slice[0])
        if validSequence(slice[0]):
            response = 'OK\n'

            s1 = Seq(slice[0])
            for i in range(1, len(slice)-1):
                print("Validating command", i, slice[i])
                r = analyse(s1, slice[i])
                response = response + str(r) + '\n'

        else:
            response = 'ERROR'
    print('Request message: {}'.format(msg))
    cs.send(str.encode(response))

# MAIN PROGRAM
# the main program I used is provided by the teacher.

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)