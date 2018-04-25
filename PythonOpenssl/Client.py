import ssl
import socket


#ip  = socket.gethostbyname(socket.gethostname())
ip = 'localhost'
port = 12345



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket = ssl.wrap_socket(server_socket, keyfile=None, certfile=None, server_side=False, ca_certs=None,do_handshake_on_connect=True, suppress_ragged_eofs=True, ciphers=None)


ssl_socket.connect((ip,port))

print "Connection Accepted\n\n"


while (True):
	
	
	you = raw_input("you: ")
	ssl_socket.send(you)
	server = ssl_socket.recv(1024)
	print server





