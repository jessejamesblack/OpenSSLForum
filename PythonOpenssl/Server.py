import ssl
import socket
import thread
import hashlib, uuid
from threading import Lock


threadLock = Lock()

SALT = 'a20330547b594ce1b60aa2f1c57cc968'

def client_connection(client_socket, client_address):

	print "Client Connection", client_address

	prompt = "Enter Your Username And Password saperted by a comma. EX john,john123"
	client_socket.send(prompt)
		
	#recive user name and password
	u_p = client_socket.recv(2000)
		
	print u_p

	#if exists send the group
	if prompt == "imran":
		print "something in there"

	else:

		prompt = "Create you Username And password saperated by a comma. EX: john,john123"
		client_socket.send(prompt)
		
		#recive user name and password
		u_p = client_socket.recv(2000)
		
		hashed_info = hashlib.sha512(u_p + SALT).hexdigest()
		print u_p
		print hashed_info

		#append hashed information to the file
		threadLock.acquire()

		temp = open("user.txt", "a")
		temp.write(hashed_info)
		temp.close()

		threadLock.release()



		client = ""

	while (True):

		
		
		
		if (client == "q"):
			client_socket.close()
			break
		you = raw_input("you: ")
		print you
		client_socket.send(you)




#retrieving data from files and formatting it properly
groups = open("groups.txt")
users = open("user.txt")

group_data = groups.readlines()
user_data = users.readlines()

groups.close()
users.close()

groups = []
users = []
for line in group_data:

	groups.append(line.strip())

for line in user_data:

	users.append(line.strip())
print "File Data Retrieved ----------------------------------------------\n"
print groups
print users
print "\nFile Data Finished -----------------------------------------------"
#finished retrieving data from files


ip  = socket.gethostbyname(socket.gethostname())
#ip = 'localhost'
port = 12345




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket = ssl.wrap_socket(server_socket, keyfile="domain.key", certfile="domain.crt", server_side=True,ca_certs=None,do_handshake_on_connect=True, suppress_ragged_eofs=True, ciphers=None)

print "\n\nbinding: " , (ip,port)
ssl_socket.bind((ip,port))
print "binding complete: " ,(ip,port)


print "\n\nListening: ", 5
ssl_socket.listen(5)


while True:
	try:
		
		
		thread.start_new_thread(client_connection,ssl_socket.accept())

		
	except Exception as e:

		print "Certification Failed"
		ssl_socket.close()
		print e.args
		break






