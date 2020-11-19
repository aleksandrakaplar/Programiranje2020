print("====================================")
print("1.Defining an empty dictionary")
dict = {}
print(dict)

print("\n====================================")
print("2. Defining a dictionary with key-value pairs")
print("Each student is defined with a unique identifier\n "
      "which is presented as the key and a value that\n "
      "represents their first and last name")
students = {
    "1": "Pera Peric",
    "2": "Zika Zika",
    "3": "Sima Simic",
    # "1": "Laza Lazic" # what will happen if we uncomment this key-value pair?
}

students["5"] = "Nikola Nikolic"

print(students)

print("\n====================================")
print("3. Accessing elements in dictionary")

print("students['1']", students["1"])
print("students['3']", students['3'])
print("students.get(2)", students.get("2"))

# Uncomment next line to see what will happen if we try to
# access with a key that is not defined in the dictionary
# print("student['4']", students['4'])

print("\n====================================")
print("4. Change values of specific item")
print("Before change")
print(students)
students["2"] = "Jelena Jelic"
# What happens if we uncomment the next line
# students["4"] = "Zika Zikic"
print("After change")
print(students)

print("\n====================================")
print("5. List all elements")

print("List all elements with: dict.keys()")
# dict.keys() returns a list of keys
for key in students.keys():
    print(students[key],'\n', end="")

print("List all elements with: dict.items()")
# dict.items() returns a list of (key, value) tuple pairs
for key, value in students.items():
    print(key, value, '\n', end="")

print("List all elements with: dict.values()")
# dict.values() returns a list of values
for value in students.values():
    print(value, '\n', end="")

print("\n====================================")
print("6. Other useful dictionary methods")

# update() method inserts an item to the dictionary
print("Update students: dict.update({key:value})")
students.update({"4" : "Mika Mikic"})
students.update({"1" : "Mika Mikic"})
print(students)

print("Copy students: dict.copy()")
# copy() returns a shallow copy of dict
new_students = students.copy()
new_students["1"] = "Nina Ninic"

print("Students:")
print(students)
print("New Students:")
print(new_students)

print("\n====================================")
print("7. Delete dictionary elements")

# removes last inserted item, in versions before 3.7
# removes random element
print("removes last inserted item")
students.popitem()
print(students)

del students['2'] # remove entry with key '2'
print("remove entry with key '2'")
print(students)

print("remove entry with key '1'")
students.pop('1') # remove entry with key '1'
print(students)

# What happens if we uncomment the next line
# students.pop('4') # remove entry with key '4'

print("Empty dictionary")
students.clear()
print(students)
