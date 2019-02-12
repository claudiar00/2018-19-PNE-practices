import socket
from Seq_p2 import Seq

#SERVER IP, PORT

IP = '192.168.0.60'
PORT = 8098

while True:
    sequence = input('Please insert a sequence: ')
    s1 = Seq_p2(sequence)
    s2 = s1.complement()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(s2.strbase()))
    msg = s.recv(2048).decode('utf-8')
    print('MESSAGE FROM THE SERVER: /n')
    print(msg)
    s.close()






