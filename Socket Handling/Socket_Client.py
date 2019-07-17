'''
Title : Python Socket Handling - Client
Author : R M Lakruwan @ Noone
Date : 17 July 2019
Compatibality : Python 3
version : 1.0
'''

# Sockets  enable programs to send and receive data
#   bi-directionally, at any given moment. 
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8081))

# Since Python 3 use Unicord str we had to encode it to bites to send
# and decode to process
def enc(txt) :
    return txt.encode('utf-8')

def den(txt) :
    return txt.decode('utf-8')

data= enc('Im Client \n')
client.sendall(data)

# Responce Handling
from_server = client.recv(4096)
client.close()

receive = den(from_server)
print(receive)

# You need two terminals to run both scripts. First Server script shoud run
# For lisning. then You can run client scripts


