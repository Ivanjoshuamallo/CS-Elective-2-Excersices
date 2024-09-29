#Ivan Joshua Mallo - Exercise 2

# Task 1: Create a Python program to perform arithmetic operations (Addition, Subtraction, Division, Multiplication, Modulus, Exponent) using two variable numbers for int, float, and complex

# Arithmetic operations on integers
int_num1 = 24
int_num2 = 2

print("Integer Operations:")
print(f"Addition: {int_num1} + {int_num2} = {int_num1 + int_num2}")
print(f"Subtraction: {int_num1} - {int_num2} = {int_num1 - int_num2}")
print(f"Multiplication: {int_num1} * {int_num2} = {int_num1 * int_num2}")
print(f"Division: {int_num1} / {int_num2} = {int_num1 / int_num2}")
print(f"Modulus: {int_num1} % {int_num2} = {int_num1 % int_num2}")
print(f"Exponent: {int_num1} ** {int_num2} = {int_num1 ** int_num2}\n")

# Arithmetic operations on floats
float_num1 = 10.5
float_num2 = 5.2

print("Float Operations:")
print(f"Addition: {float_num1} + {float_num2} = {float_num1 + float_num2}")
print(f"Subtraction: {float_num1} - {float_num2} = {float_num1 - float_num2}")
print(f"Multiplication: {float_num1} * {float_num2} = {float_num1 * float_num2}")
print(f"Division: {float_num1} / {float_num2} = {float_num1 / float_num2}")
print(f"Modulus: {float_num1} % {float_num2} = {float_num1 % float_num2}")
print(f"Exponent: {float_num1} ** {float_num2} = {float_num1 ** float_num2}\n")

# Arithmetic operations on complex numbers
complex_num1 = 1 + 3j
complex_num2 = 2 + 4j

print("Complex Number Operations:")
print(f"Addition: {complex_num1} + {complex_num2} = {complex_num1 + complex_num2}")
print(f"Subtraction: {complex_num1} - {complex_num2} = {complex_num1 - complex_num2}")
print(f"Multiplication: {complex_num1} * {complex_num2} = {complex_num1 * complex_num2}")
print(f"Division: {complex_num1} / {complex_num2} = {complex_num1 / complex_num2}\n")
# Note: Modulus and Exponent are not used with complex numbers in this way

# Task 2: Write a program that creates two variables, num1 and num2. Both num1 and num2 should be assigned the integer literal 25000000, one written with underscores and one without.

# Creating variables with and without underscores
num1 = 25_000_000
num2 = 25000000

print("Variables with and without underscores:")
print(f"num1 with underscores: {num1:_}")  # Displays the number with underscores
print(f"num2 without underscores: {num2}\n")

# Task 3: Creating int, float, and complex variables then checking their types

# Creating int, float, and complex variables
int_var = 10
float_var = 3.14
complex_var = 2 + 3j

# Checking and printing their types
print("Variable Types:")
print(f"Type of int_var: {type(int_var)}")    # Output: <class 'int'>
print(f"Type of float_var: {type(float_var)}")  # Output: <class 'float'>
print(f"Type of complex_var: {type(complex_var)}\n") # Output: <class 'complex'>
