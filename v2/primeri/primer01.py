print("Example 01 - Reading content from txt file:")

# <variable> = open(<name>, <mode>, <encoding>)
# name - name of file on the disk
# mode - "r", "w" or "a" depending on if we want to read, write or append content. We can also specifiy if we want to open a file in text or binary mode. Default value is 'r' - read
# encoding - recommended to specifiy encoding type  'utf-8'

file = open("files/example01.txt")

# read a file
# <file>.read(<size>)
# size - number of characters to read 

print('Read first 5 characters in file:' + file.read(5)) # read the first 5 data
print("Read the next 3 characters in file:" + file.read(3)) # read the next 4 data

print('Current cursor position in file:' + str(file.tell())) # returns are current position 
print('Set file cursor to beginning of file')
file.seek(0) # bring file cursor to initial position

print('\nRead all file content:')
print(file.read()) # without an argument for size, read the entire file

# Closing files 

file.close()

print("\nExample 02 - Reading content from txt file:")

file = open("files/example01.txt")

# reading file content with for loop
for line in file: 
    print(line, end = "")

file.close()

print("\n\nExample 03 - Reading content from txt file:")

file = open("files/example01.txt")

print(file.readlines())

file.close()

print("\nExample 04 - Writing content to txt file")

# in order to write into a file mode must be w, a or x
# 'w' overwrites existing content in file
file = open("files/example02.txt", "w", encoding = 'utf-8')

file.write("First line\n")
file.write("Second line\n")
file.write("Last line\n")

file.close()

print("\nExample 05 - Append content to txt file that exists")

file = open("files/example02.txt", "a", encoding = 'utf-8')
file.write("Last line for real\n")

file.close()

print("\nExample 06 - Append content txt file that does not exist")

file = open("files/example03.txt", "a", encoding = 'utf-8')
file.write("New File\n")

file.close()

print("\nExample 07 - Write binary file")

file = open("files/example_string.bin", "wb")

file.write(bytes("Read this line in binary fajl", encoding='utf-8'))

file.close()

file = open("files/example_array.bin", "wb")
nums = [1, 2]
file.write(bytearray(nums))

file.close()

print("\nExample 08 - Read binary file")

file = open("files/example_string.bin", "rb")
read_string = file.read()

print(read_string.decode('utf-8'))

file.close()

file = open("files/example_array.bin", "rb")
read_nums = file.read()
nums = list(read_nums)

print(nums)

file.close()

print("\nExample 09 - Read/Write a list to a txt file")
colors = ['blue', 'green']

# try to set mode to w+ and
file = open("files/colors.txt", "w")

for color in colors:
    file.write(color + ";")

# try to comment these two lines. What happens?  
file.close() 
file = open("files/colors.txt", "r")

read_file = file.read()
print("In file:", read_file)

file.close()
