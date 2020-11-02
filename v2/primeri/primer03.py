print("Example 02 - Dictionary")

print("Defining a dictionary")
# dic = { key1: value1, key2: value2 }
students = {
    "index1": "Stundet 1", 
    "index2": "Stundet 2", 
    "index3": "Stundet 3", 
    "index4": "Stundet 4",
}
print("Show dictionary: ", students)
# dic[key] -> returns value
print("Get student with index1 ", students["index1"])
print("Get student with index2 ", students["index2"])

print("Change value in dictionary")
students["index1"] = "New Student 5"
print(students)