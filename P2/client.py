import socket
from Seq import Seq

#SERVER IP, PORT

IP = '127.0.0.1' #I have put here my computers IP
PORT = 8090

while True:
    sequence = input('Please insert a sequence: ')
    s1 = Seq(sequence)
    comp = s1.complement()
    reverse = s1.reverse()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode('\n The complement sequence: '))
    s.send(str.encode(comp.strbase))
    s.send(str.encode('\n The reverse sequence: '))
    s.send(str.encode(reverse.strbase))
    msg = s.recv(2048).decode('utf-8')
    print('MESSAGE FROM THE SERVER: /n')
    print(msg)
    s.close()






