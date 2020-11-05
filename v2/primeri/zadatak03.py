list_of_items = []

with open('files/zadatak02.txt') as f:
    for line in f.readlines():
        items = line.split('|')
        for item in items: 
            if item != '':
                list_of_items.append(item)
        
print(list_of_items)