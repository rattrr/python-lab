import sys
import re
import socket

inputfile = sys.argv[1]

with open(inputfile, 'r') as f:
	from_file = f.read()

result = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", from_file)
print result

for ip in result:
	try:
		socket.inet_aton(ip)
		print ip
	except:
		pass


