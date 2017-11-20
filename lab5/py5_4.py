import re

test_pesel = "44051401458"

regex_pesel = re.compile(r'(?P<bdate>\d{6})(?P<rest>\d{5})')

def validate(pesel):
	if len(pesel) != 11:
		return False
	if str(9*int(pesel[0]) + 7*int(pesel[1]) + 3*int(pesel[2]) + int(pesel[3]) + 9*int(pesel[4])
	+ 7*int(pesel[5]) + 3*int(pesel[6]) + int(pesel[7]) + 9*int(pesel[8])
	+ 7*int(pesel[9]))[-1] == pesel[10][-1]:
		return True

def get_data(pesel):
	for match_object in regex_pesel.finditer(pesel):
		data = match_object.groupdict()

	pesel_data = dict.fromkeys(["bdate", "sex"], None)

	bdate = data.get('bdate')
	pesel_data['bdate'] = "{}.{}.{}".format(bdate[0:2], bdate[2:4], bdate[4:6])

	male = (1, 3, 5, 7, 9)
	if data.get('rest')[-2] in male:
		pesel_data['sex'] = 'male'
	else:
		pesel_data['sex'] = 'female'

	return pesel_data

if validate(test_pesel):
	print "birthday: {}\nsex: {}".format(get_data(test_pesel)['bdate'], get_data(test_pesel)['sex'])
else:
	print "PESEL not correct"
