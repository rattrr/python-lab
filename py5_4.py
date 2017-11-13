import re

test_pesel = "44051401458"

regex_pesel = re.compile(r'(?P<bday>\d{6})(?P<rest>\d{5})')

for match_object in regex_pesel.finditer(test_pesel):
	data = match_object.groupdict()

bdate = data.get('bday')
male = (1, 3, 5, 7, 9)

print "{}.{}.{}".format(bdate[0:2], bdate[2:4], bdate[4:6])
if data.get('rest')[-2] in male:
	print "male"
else:
	print "female"
