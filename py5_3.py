import sys
import re
import socket


def filterCorrectIPs(iptable):
	correctip = list()
	for ip in iptable:
		try:
			socket.inet_aton(ip)
			correctip.append(ip);
		except:
			print "{} is not correct.".format(ip)
	return correctip

inputfile = sys.argv[1]

with open(inputfile, 'r') as f:
	from_file = f.read()

result = filterCorrectIPs(re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", from_file))
print result
