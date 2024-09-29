# Task 1: Calculate the Length of a String
string = "Boss Ivan Cute"
length = len(string)
print(f"Task 1 - The length of the string is: {length}")

# Task 2: Count the Number of Characters in a String
character_count = len(string)
print(f"Task 2 - The number of characters in the string is: {character_count}")

# Task 3: Replace All Occurrences of the First Char with '$' (Except the First Char Itself)
def replace_char(s):
    first_char = s[0]
    replaced_string = first_char + s[1:].replace(first_char, '$')
    return replaced_string

input_string = "restart"
result = replace_char(input_string)
print(f"Task 3 - Modified string: {result}")

# Task 4: Swap the First Two Characters of Each String and Concatenate Them
def swap_first_two_chars(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return f"{new_str1} {new_str2}"

string1 = "Sete"
string2 = "Cunsei"
swapped_result = swap_first_two_chars(string1, string2)
print(f"Task 4 - Swapped and concatenated string: {swapped_result}")

# Task 5: Concatenate Strings Using Four Variables
str1 = "Hello"
str2 = "my"
str3 = "name"
str4 = "Boss Ivan"
concatenated_string = str1 + " " + str2 + " " + str3 + " " + str4
print(f"Task 5 - {concatenated_string}")

# Task 6: Concatenate Strings from User Input
string1 = input("Task 6 - Enter the first string: ")
string2 = input("Task 6 - Enter the second string: ")
concatenated_input = string1 + " " + string2
print(f"Task 6 - Concatenated string: {concatenated_input}")

# Task 7: Concatenate Name and Age in a Paragraph
# Define the variables
name = "Ivan Joshua Mallo"
age = 21

# Concatenate using the + operator
paragraph = "Hello, my name is " + name + " and I am " + str(age) + " years old."
print("Task 7 - " + paragraph)

