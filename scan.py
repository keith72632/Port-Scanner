import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
	print('target is {}'.format(target))
else:
	print('invalid target')
	sys.exit()

print('-' * 50)
print('[+]Scanning target: {}'.format(target))
print('[+]Time started {}'.format(datetime.now()))
print('-' * 50)

try: 
	for port in range(50, 85):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = sock.connect_ex((target, port))
		print("[+]Checking port {}".format(port))
		if result ==0:
			print("[+]Port {} is open".format(port))
		sock.close()

except KeyboardInterrupt:
	sys.exit()

except socket.gaierror:
	print('[x]couldnt resolve hostname')
	sys.exit()

except socket.error:
	print('[x]couldnt connect to server')
	sys.exit()