line = ''
sum = 0
items = 0

file = open('patient_data.csv')
for n in file:
	line = n.split(',')
	sum += int(line[1])
	items += 1
file.close()

print(sum/items)
