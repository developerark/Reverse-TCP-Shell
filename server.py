import socket 
import sys

arguments = sys.argv

def startListenerOnPort(port, host='127.0.0.1'):
	"""Starts a listener on the specific port"""
	try:
		socketObj = socket.socket()
	except Exception as error:
		print "[!] Error: Cannot create a socket object"
		sys.exit()
	socketObj.bind((host, port))
	socketObj.listen(1)
	print "Listening on host " + host + " port " + str(port)
	connection, address = socketObj.accept()
	print "[+] Connection From: " + str(address)
	return connection

if __name__ == "__main__":
	if len(arguments) > 2:
		print "[!] Error: Too many arguments"
		sys.exit(0)
	elif len(arguments) == 2:
		# Port provided in the arguments
		try:
			port = int(arguments[1])
		except Exception as error:
			print "[!] Error: Port number should be an integer"
			sys.exit(0)
	else:
		# Default port for the listener assigned to 8080
		port = 8080


	connection = startListenerOnPort(port)

	# If connection was successfully created
	if connection:
		while True:
			command = raw_input(connection.recv(1024))
			if command == 'quit':
				connection.close()
				sys.exit(0)
			if len(command) > 0:
				connection.send(command)
				#response = connection.recv(1024)
				#ls
				print response



