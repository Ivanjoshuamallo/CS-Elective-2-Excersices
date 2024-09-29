# Function that checks if a number is greater than 10
def check_greater_than_10(num):
    if num > 10:
        return True
    else:
        return False

# Test the function
number = 15
result = check_greater_than_10(number)
print(f"Is {number} greater than 10? {result}")

# Example collections with different data types (str, int, bool)
# List
my_list = ["Hello", 123, True, "World", 456, False]
print("List:", my_list)

# Tuple
my_tuple = ("Python", 789, False, "Coding", 101, True)
print("Tuple:", my_tuple)

# Set
my_set = {"SetExample", 555, True, "UniqueValues", False, 789}
print("Set:", my_set)

# Dictionary
my_dict = {
    "name": "Ivan",
    "age": 21,
    "is_student": True,
    "height": 175,
    "enrolled": False
}
print("Dictionary:", my_dict)

# Accessing elements from each collection
print("\nAccessing specific elements:")
print("List first element:", my_list[0])
print("Tuple second element:", my_tuple[1])
print("Check if 'SetExample' is in Set:", "SetExample" in my_set)
print("Dictionary 'name' key:", my_dict["name"])
