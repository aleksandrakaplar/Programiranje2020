# if - else statement
print("Example01: Compare numbers:")
num1 = input("Insert a number:")
num2 = input("Insert a number:")

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

print("===========================================")
print("Example02: While Loop")

while True:
    print("1. Hi")
    print("2. How is the day today?")
    print("3. Bye")
    str_input = input("Select option>>>")
    if str_input == "1":
        print("Hi!")
    elif str_input == "2":
        print("Nice Day!")
    else:
        print("Good Bye!")
        break

print("===========================================")
print("Example02: For Loop")

str_input = "This is our test string"
print("String:")
for char in str_input:
    print(char, end=" ")

print("\nExample 1 numbers from 0 to 4")
for i in range(5): # range object, stores a sequence of numbers
    print(i)

print("Example 2 numbers from 0 to 4")
for i in range(0, 5):
    print(i)

print("Example 3 even numbers to 10")
for i in range(0, 12, 2):
    print(i)