import socket
from Seq import Seq

#SERVER IP, PORT

IP = '79.159.207.230'
PORT = 8081

while True:
    sequence = input('Please insert a sequence: ')
    s1 = Seq(sequence)
    s2 = s1.complement()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(s2.strbase()))
    msg = s.recv(2048).decode('utf-8')
    print('MESSAGE FROM THE SERVER: /n')
    print(msg)
    s.close()






