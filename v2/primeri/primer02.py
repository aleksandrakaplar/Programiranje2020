print("Example 01 - Sets")

print("Creating an empty set ")
basket = set()
print(basket)

print("Adding items to set (apple, apple)")
basket.add('apple')
basket.add('apple')

print("Adding 3 items at once to set")
basket.update(['apple', 'orange', 'cherry'])
print("1. Show all items from set")
print(basket)
print("2. Show all items from set")
for item in basket: 
    print(item)
    
print("Creating new set of items")
basket = {'apple', 'orange', 'apple', 'grapes'}

print("Show all items from set")
print(basket)

print('Apple in basket? ' + str('apple' in basket))
print('Potato in basket? ' + str('potato' in basket))

# remove, discard, pop
print("Removing items from basket (apple and banana)")
basket.remove('apple')
# basket.remove('banana') # this will return an error if item does not exist in set
basket.discard('banana') # this will not return an error if item does not exist in set
print(basket)
print("Remove last item")
last_item = basket.pop() # sets are unordered, we do not know which item is removed
# first_item = basket.pop(1) # this will return an error
print("Removed item", last_item) 
print(basket)

print("Join two Sets: A U B")
A = {'a', 1, 'b'}
B = {'c', 1, 'd'}

C = A.union(B)
print(C)

print("Intersection of two Sets:")
C = A.intersection(B)
print(C)

print("Difference between two sets")
C = A.difference(B)
print("Difference between A and B set ", C)
C = B.difference(A)
print("Difference between B and A set ", C)

C = B.symmetric_difference(A)
print("Simetric Difference between B and A set ", C)

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
