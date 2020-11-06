f = open('files/zadatak01.txt')

char_find = input("Which character do you wish to find >>>")
numb = 0

for line in f:
    for char in line:
        if char == char_find:
            numb = numb + 1

print(f'The number of times the character {char_find} was {numb}')
# print('The number of times the character ' + char_find + ' was ' + str(numb))

# Python string count 
f.seek(0)
# print(f.tell())
file_text = f.read()
print(file_text)
numb = file_text.lower().count(char_find.lower())
print(f'The number of times the character {char_find} was {numb}')

f.close()
