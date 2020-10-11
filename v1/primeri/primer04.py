colors = []


def print_list():
    print("Colors:")
    for color in colors:
        print(color)
    print()


def return_example():
    text_test = "This is a returned string!"
    return text_test


# Whenever the Python interpreter reads a source file
# it sets a few special parameters __name__
# it executes the code found in the file
if __name__ == '__main__':
    colors = ["blue", "purple", "green"]
    print_list()

    colors.append("red")
    print_list()

    colors.insert(0, "red")
    print_list()

    print(return_example())
