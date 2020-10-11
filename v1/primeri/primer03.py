print("Example01: List")

colors = ["blue", "purple", "green"]

print("1. Elements in list colors")
print(colors)

print("2. Elements in list colors")
for i in range(len(colors)):
    print(colors[i])

print("3. Elements in list colors")
for color in colors:
    print(color)

print("First element in list: " + colors[0])
print("Last element in list: " + colors[-1])

print("Change first element")
colors[0] = input("Insert a color>>>")
print("2. Elements in list colors")
for i in range(len(colors)):
    print(colors[i])

print("Example02: Advance List Functions")
colors = ["blue", "purple", "green"]

colors.append("red")
print("Add red as last color")
for color in colors:
    print(color)

colors.insert(0, "red")
print("Add red as first color")
for color in colors:
    print(color)

print("Number of red colors: " + str(colors.count("red")))
print("Index of red color: " + str(colors.index("red")))

print("Remove red")
# Will all the red colors be removed from the list?
colors.remove("red")
for color in colors:
    print(color)

print("Color red exists? " + str("red" in colors))
print("Remove last element")
colors.pop()
print("Color red exists? " + str("red" in colors))

print("Total number of colors " + str(len(colors)))

colors.sort()
print("Sorted colors (ascending):")
for color in colors:
    print(color)

colors.reverse()
print("Reverse colors (descending):")
for color in colors:
    print(color)

print("===========================================")
print("Example 03: Copy list")

colors = ["blue", "purple", "green"]
new_colors = colors.copy()
new_colors.insert(0, "brown")
print("List of old colors:")
for color in colors:
    print(color)
print("List of new colors:")
for color in new_colors:
    print(color)

print("===========================================")
print("Example 04: Tuple")
# Tuples are immutable

coordinates = (1, 2, 1)
# coordinates[1] = 10 Error
print(coordinates[0], coordinates[1])
print("Number of 1:" + str(coordinates.count(1)))
print("Index of 1:" + str(coordinates.index(1)))
# List of Tuples
coordinates = [(1, 2), (2, 1)]
