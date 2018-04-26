import ssl
import socket
import pprint

#ip  = socket.gethostbyname(socket.gethostname())
ip = '128.6.13.206'
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
	print "Connection Accepted\n\n"
	while (True):
		you = raw_input("you: ")
		ssl_socket.send(you)
		server = ssl_socket.recv(1024)
		if server == 'q':
				ssl_socket.close()
		print server
except ssl.CertificateError:
	print "Certification failed"








