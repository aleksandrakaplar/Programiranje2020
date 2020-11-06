list_of_items = []

f = open('nazivFajla', 'w+')

with open('files/zadatak02.txt') as f:
    # 'blue|green|...', ' ']
    for line in f.readlines():
        # line = 'blue|green|yellow|brown|'
        # line_split = line.split('|')
        # line_split = ['blue', 'green', 'yellow', 'brown', '']
        # line_split[0], line_split[1]
        items = line.split('|')
        # items = ['blue', 'green', ..., '']
        for item in items:
            if item != '':
                list_of_items.append(item)
        
print(list_of_items)
