knjige = [
	{'sifra': '1', 'naslov': 'A', 'autor': 'C', 'godina': 2000 },
	{'sifra': '2', 'naslov': 'C', 'autor': 'A', 'godina': 2101 },
	{'sifra': '3', 'naslov': 'B', 'autor': 'B', 'godina': 2020 }
]

def bubble_sort(key, list_od_dicts):
	new_list = list_od_dicts.copy()
	swaps = 1 # True
	while swaps != 0: # while swaps:
		swaps = 0 # swaps = False
		for i in range(len(new_list) - 1):
			if new_list[i][key] > new_list[i+1][key]:
				temp = new_list[i]
				new_list[i] = new_list[i+1]
				new_list[i+1] = temp
				swaps += 1 # swaps = True
	return new_list
	
print('Sort po godini (rastuce):', bubble_sort("godina", knjige))
print('Sort po autoru (rastuce):', bubble_sort("autor", knjige))
print('Sort po naslovu (rastuce):', bubble_sort("naslov", knjige))
				
