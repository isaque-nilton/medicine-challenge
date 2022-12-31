line = ''
disease = ''
dict = {}

file = open('patient_data.csv')
for n in file:
	line = n.split(',')
	disease = line[2][:-1]
	if disease in dict:
		dict[disease] += int(line[1])
		dict[disease+'-n'] += 1
	else:
		dict[disease] = int(line[1])
		dict[disease+'-n'] = 1
file.close()

for i in dict:
	if '-n' not in i:
		dict[i] /= dict[i+'-n']
		print('Average age for '+i+' diagnosis: '+str(dict[i]))
