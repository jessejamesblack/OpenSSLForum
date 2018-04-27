import ssl
import socket
import pprint
import re
import time

ip  = socket.gethostbyname(socket.gethostname())
#ip = '128.6.13.206'
port = 13333

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket = ssl.wrap_socket(server_socket, keyfile=None, certfile=None, server_side=False, 
	ca_certs=None,do_handshake_on_connect=True, suppress_ragged_eofs=True, ciphers=None)

try:
	context = ssl.create_default_context()
	#context = ssl.SSLContext()
	context.verify_mode = ssl.CERT_REQUIRED
	context.check_hostname = True
	context.load_verify_locations("domain.crt")
	ssl_socket = context.wrap_socket(server_socket, server_hostname='first')
	ssl_socket.connect((ip,port))
	cert = ssl_socket.getpeercert(binary_form=False)
	pprint.pprint(cert)
	print "Connection Accepted\n\n"
	username = "" # you will have username and password in an array when the authentication loop breaks . ex: username = [jesse,123]
	#this loop completes the authentication part , and it breaks when the authentication Completes
	while (True):
		server = ssl_socket.recv(1024)
		if server == "T":

			server = ssl_socket.recv(1024)

			print "Password Authentication Complete"
			print server
			break


		print server


		you = raw_input("Your Command$> ")
		ssl_socket.send(you)

	#this is used for communication for GET,POST, END methods
	#it should sanitize user input!!
	#it should add the username and time to the message!!
	while (True):
		
		you = raw_input("Your Command$> ")

		if you.lower() == "end":
    			ssl_socket.close()
			break

		if you.lower().find("get") == -1:
    			print "Incorrect syntax."
			if you.lower().find("post") == -1:
    				print "Incorrect syntax."
		
		if you.lower().find("post") == 0:
				ssl_socket.send(you + " " + time.ctime())

		if you.lower().find("get") == 0:
    			ssl_socket.send(you)
		
		

		server = ssl_socket.recv(1024)
		print server
		
except ssl.CertificateError as e:
	print "Certification failed"


