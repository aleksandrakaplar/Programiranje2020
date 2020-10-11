print("Example 01: print example")
print("Hello, Uncle Bob!")
print("Uncle Bob has great programming skills.")
print("Be like Uncle Bob")
print("===========================================")

print("Example 02:Declaring variables")
name = "Sara"
# string concatenation
print("Hello " + name + "!")
print(name + " has great programming skills.")
print("Be like " + name)
print("===========================================")

# special characters \n \t \"
print("Example 03: Special characters \ n \ t \\\"")
name = 'John'
print("Hello " + name + "!" + "\n" + name + " has \"great\" programming skills.\nBe like " + name)
print("===========================================")

print("Example 04: User input")

name = input("Please insert your name:")
age = input("Please insert your age:")
print("Hello " + name + " age: " + age)

print("===========================================")
print("Example 05:Advance string operations")

test_text = "This is an example text."

print("Lower case example:")
print(test_text.lower())
print(test_text)

print("Upper case example:")
print(test_text.upper())
print(test_text)

print("First character of test_text is: " + test_text[0])
print("Last character of test_text is: " + test_text[len(test_text) - 1])

print("When we replace an example with a: " + test_text.replace("an example", "a"))

print("===========================================")

print("Example 06: Arithmetic operations (+, -, *, /, %)")
side_a = 5
side_b = 2
rectangle_perimeter = 2 * side_a + 2 * side_b
# rectangle_perimeter = 2 * (side_a+side_b)
print("The perimeter of the rectangle is " + str(rectangle_perimeter))

number = 5
is_even = number % 2 == 0
print("Number " + str(number) + " is even? " + str(is_even))

print("===========================================")

print("Example 07: Advance number operations")

print("Maximum number: " + str(max(5, 2)))
print("Minimum number: " + str(min(5, 2)))
print("Absolut value: " + str(abs(-5)))
print("Round value: " + str(round(-5.5)))
print("Round value: " + str(round(-5.4)))

# print("Square root of 4: " + str(sqrt(4))) - Error
from math import * # importing functions from math module
print("Square root of 4: " + str(sqrt(4)))
print("Round up: " + str(ceil(4.1)))

print("===========================================")
print("Example 08: Comparison Operators (>, >=, <, <=, ==, !=)")

num1 = 2
num2 = 4

is_greater = num1 > num2
is_less = num1 < num2
is_equal = num1 == num2
is_not_equal = num1 != num2

print("Is " + str(num1) + " > " + str(num2) + " = " + str(is_greater))
print("Is " + str(num1) + " < " + str(num2) + " = " + str(is_less))
print("Is " + str(num1) + " == " + str(num2) + " = " + str(is_equal))
print("Is " + str(num1) + " != " + str(num2) + " = " + str(is_not_equal))

print("===========================================")
print("Example 09: Logical Operators (and, or, not)")

num = 10
print(num >= 0 and num <= 10)

print("===========================================")
print("Example 10: Bit Operations (&, |, ^, ~, <<, >>)")
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b;        # 12 = 0000 1100
print("result of AND is ", c,':',bin(c))

c = a | b;        # 61 = 0011 1101
print("result of OR is ", c,':',bin(c))

c = a ^ b;        # 49 = 0011 0001
print("result of EXOR is ", c,':',bin(c))

c = ~a;           # -61 = 1100 0011
print("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;       # 240 = 1111 0000
print("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;       # 15 = 0000 1111
print("result of RIGHT SHIFT is ", c,':',bin(c))

print("===========================================")
print("Example 11: Calculator Example")

num1 = input("Enter a number:")
num2 = input("Enter another number:")

result = num1 + num2
# is the result correct?
print("Result " + num1 + " + " + num2 + " = " + result)

# typecasting, error if decimal number is inserted!
result = int(num1) + int(num2)
print("Result " + num1 + " + " + num2 + " = " + result)

result = float(num1) + float(num2)
print("Result " + num1 + " + " + num2 + " = " + result)
