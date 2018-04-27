import ssl
import socket
import thread
import hashlib, uuid
from threading import Lock
import Group as g
import helper as h
import os.path

#all group information in "groups" and all the users information in "users"
groups = []
users = []
groups_name= ""
threadLock = Lock()
SALT = 'a20330547b594ce1b60aa2f1c57cc968'
message  = "\tGET,<group_name> //gets all messages from the specified group.\n\tPOST,<group_name>,<message> // posts the message on the specified group\n\tEND //end my session with the server"

def update_group(group):

	size  = groups.__len__()
	i = 0

	while i < size:
	
		each = groups[i]
		if (each.getGroupName() == group.getGroupName()):

			groups[i] = group
		i+=1
	return groups


def validate_group_name(name):
	
	for group in groups:

		if (group.getGroupName().lower() == name):

			return group
	return None
def validate_user(hashed_info):
	
	for user in users:

		
		if user == hashed_info:

			return True
	return False
	

def client_connection(client_socket, client_address):

	print "Client Connection: ", client_address

	prompt = "\nEnter Your Username And Password saperted by a comma. EX john,john123\n"
	client_socket.send(prompt)
		
	#recive user name and password
	u_p = client_socket.recv(2000)	
	hashed_info = hashlib.sha512(u_p + SALT).hexdigest()

	validation = validate_user(hashed_info)

	status = "F"
	#if exists send the group
	if validation:
		print "Password Validation Successfull for: " , client_address
		status = "T"
		client_socket.send(status)

	else:

		prompt = "\nCreate you Username And password saperated by a comma. EX: john,john123\n"
		client_socket.send(prompt)
		
		#recive user name and password
		u_p = client_socket.recv(2000)
		
		hashed_info = hashlib.sha512(u_p + SALT).hexdigest()
		
		while (validate_user(hashed_info) == True ):

			prompt = "\nUser Already Exists.\nCreate Different Username And password saperated by a comma. EX: john,john123\n"
			client_socket.send(prompt)

			u_p = client_socket.recv(2000)
			hashed_info = hashlib.sha512(u_p + SALT).hexdigest()

		status = "T"
		client_socket.send(status)			
		#append hashed user information to the file
		threadLock.acquire()
		temp = open("user.txt", "a")
		temp.write(hashed_info + "\n")
		temp.close()
		threadLock.release()
		#append to the user array
		users.append(hashed_info)

	

	
	#Connection And Verfication Complete with the client
	print "Sending Group Names to: " , client_address
	client_socket.send("Group Names:\n" + groups_name+"\n" +message )

	client = client_socket.recv(2000)
	client = client.lower()

	while (True):

	
		response = client.split(",")
		#print response
		method = response[0]
		

		if client == "end":
			print  "ends: " , client_address
			client_socket.send("\tYou Session Ended. You Could Log Back in By Simply USING ANY OF THE COMMANDS GET OR POST")

		elif (method == "get"):

			group_name = response[1]
			g = validate_group_name(group_name)
			if (g != None):
				
				print "Sending Messages For Group: " , group_name, "TO: " , client_address
				new_message = "None"
				new_message = g.getMessages()
				client_socket.send(new_message + "\n\tGROUP NAMES:\n" +groups_name )
			else:

				client_socket.send("Group Name Invalid" + "\n\tGROUP NAMES:\n" +groups_name)
			
		elif (method == "post"):
	
			group_name = response[1]
			g = validate_group_name(group_name)
			if (g != None):
				
				print "Adding Message to the group: " , group_name, " BY: " , client_address


				message_n = ""
				i = 2
				while  i < response.__len__():

					if (i == 2):

						message_n = response[i]
					else:

						message_n += "," + response[i]
					i +=1
		
				print message_n
				g.addGroupMessage(message_n)

				#updating the files
				threadLock.acquire()
				groups = update_group(group)
				h.write_group_content(groups)
				threadLock.release()

				client_socket.send("Messaage Added Successfully ==> " + message_n + "\n\tGROUP NAMES:\n" +groups_name)
			else:

				client_socket.send("Group Name Invalid" + "\n\tGROUP NAMES:\n" +groups_name)
			
		
		else:
		
			client_socket.send("Unrecognized Command" + "\n\tGROUP NAMES:\n" +groups_name)
			client_socket.send("\n" +message)

		client = client_socket.recv(2000)
		client = client.lower()
		
	

	print  "ends: " , client_address
	client_socket.close()
	return
		
		
		


#checking if the files exist : user.txt and groups.txt

user_check = os.path.isfile("user.txt")
group_check = os.path.isfile("groups.txt")

if user_check == False:

	#create a user file 
	user_create = open("user.txt", "w")
	user_create.close()

else:

	users_f = open("user.txt")
	user_data = users_f.readlines()
	users_f.close()
	for line in user_data:

		users.append(line.strip())
	

if group_check == False:

	#create a groups file
	#add FOOD and CLASS group in there with #EOF
	
	groups = [g.Group("FOOD") , g.Group("CLASS")]
	h.write_group_content(groups)
else:

	#retrieving data from files and formatting it properly
	groups = h.read_group_content(groups)
	
	

for group in groups:

	groups_name += group.getGroupName() + "\n"


#print "File Data Retrieving ----------------------------------------------\n"
#print groups
#print users
#print "\nFile Data Retrieved -----------------------------------------------"
#finished retrieving data from files


ip  = socket.gethostbyname(socket.gethostname())
#ip = 'localhost'
port = 12345




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket = ssl.wrap_socket(server_socket, keyfile="domain.key", certfile="domain.crt", server_side=True,ca_certs=None,do_handshake_on_connect=True, suppress_ragged_eofs=True, ciphers=None)

##print "\n\nbinding: " , (ip,port)
ssl_socket.bind((ip,port))
##print "binding complete: " ,(ip,port)


##print "\n\nListening: ", 5
print "Server is running on port 5000..."
print "File Data Retrieving ----------------------------------------------"
print "File Data Retrieved -----------------------------------------------"
ssl_socket.listen(5)


while True:
	try:
		
		
		thread.start_new_thread(client_connection,ssl_socket.accept())
		

		
	except Exception as e:

		print "Certification Failed"
		ssl_socket.close()
		print e.args
		break






