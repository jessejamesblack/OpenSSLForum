import ssl
import socket


#ip  = socket.gethostbyname(socket.gethostname())
ip = 'localhost'
port = 12345



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket = ssl.wrap_socket(server_socket, keyfile="domain.key", certfile="domain.crt", server_side=True, ca_certs=None,do_handshake_on_connect=True, suppress_ragged_eofs=True, ciphers=None)

print "\n\nbinding: " , (ip,port)
ssl_socket.bind((ip,port))
print "binding complete: " ,(ip,port)


print "\n\nListening: ", 5
ssl_socket.listen(5)


(client_socket, client_address) = ssl_socket.accept()
print "\n\nAccepted Connection: " , (client_socket , client_address)

while (True):

	client = client_socket.recv(1024)
	print "client: " , client
	you = raw_input("you: ")
	print you
	client_socket.send(you)






