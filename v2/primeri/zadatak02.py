list_of_items = ['blue', 'green', 'yellow', 'brown']

f = open('files/zadatak02.txt', 'w')

for item in list_of_items:
	f.write(item + '|')
# blue|green|yellow|brown|

f.close()
