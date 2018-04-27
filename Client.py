import ssl
import socket
import pprint
import re
import time

ip  = socket.gethostbyname(socket.gethostname())
#ip = '128.6.13.206'
port = 12345

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
	print "\tConnection Accepted\n\n"
	username = "" # you will have username and password in an array when the authentication loop breaks . ex: username = [jesse,123]
	#this loop completes the authentication part , and it breaks when the authentication Completes
	while (True):
		server = ssl_socket.recv(1024)
		if server == "T":

			server = ssl_socket.recv(1024)

			print "\tPassword Authentication Complete"
			print server
			username = check_you[0]
			break


		print server


		you = raw_input("Your Command$> ")
		check_you = you.split(",")
		while(check_you.__len__() != 2):

			print "\tINVALID FORMAT FOR USERNAME AND PASSWORD. FOMAT ==> username,password"
			you = raw_input("Your Command$> ")
			check_you = you.split(",")


			
		ssl_socket.send(you)

	#this is used for communication for GET,POST, END methods
	#it should sanitize user input!!
	#it should add the username and time to the message!!
	while (True):
		
		wrong_input = False
		you = raw_input("Your Command$> ")
		response = you.split(",")
		#print response

		if you.lower() == "end":
			ssl_socket.send("end")
    			ssl_socket.close()
			break
	
		

		elif ((response[0].lower() == "get") and (response.__len__() == 2 )):
			group_name = response[1]
			ssl_socket.send("GET," + group_name)

		elif ((response[0].lower() == "post") and (response.__len__() >= 3)):
			group_name = response[1]
			message = "'None"
		
			i = 2
	
			while i < response.__len__():

				if ( i == 2) :
					message = "'" + response[i]
				else:
					message += ","+response[i]
				i +=1
				

			message += "'	" + username + "  " + time.ctime()
			print message
			
			ssl_socket.send(response[0] + "," + group_name + "," + message)
		else:

			print "\tINVALID FORMAT FOR YOUR COMMAND"
			wrong_input = True

		'''
		if (you.lower().find("get")) == -1:
    			print "Incorrect syntax."
			#needs to be fixed hangs without the break
			
			if you.lower().find("post") == -1:
    				print "Incorrect syntax."
		
		if you.lower().find("post") == 0:
				ssl_socket.send(you +" " + time.ctime())

		if you.lower().find("get") == 0:
    			ssl_socket.send(you)
		'''
		
		
		if (wrong_input == False):

			server = ssl_socket.recv(1024)
			print server
		
except ssl.CertificateError as e:
	print "Certification failed"


