'''
Title : Python Socket Handling - Server
Author : R M Lakruwan @ Noone
Date : 17 July 2019
Compatibality : Python 3
version : 1.0
'''

# Sockets  enable programs to send and receive data
#   bi-directionally, at any given moment. 
import socket

# The family para : Address Format Internet (Default)
# The type para : Socket Stream (default) - sequenced, reliable,
#   two-way, connection-based byte streams  over TCP1
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binds it to localhost’s port 8080 as a socket server. 
serv.bind(('0.0.0.0', 8081))
serv.listen(5)

# Since Python 3 use Unicord str we had to encode it to bites to send
# and decode to process
def enc(txt) :
    return txt.encode('utf-8')

def den(txt) :
    return txt.decode('utf-8')

while True:
    # Request Handling
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = den(conn.recv(4096))
        
        if not data: break
        from_client += data
        print(from_client)

        sen_enc = enc('I am SERVER\n')       
        conn.sendall(sen_enc)
        
    conn.close()
    print('client disconnected')


# You need two terminals to run both scripts. First Server script shoud run
# For lisning


