# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Access elements in a tuple
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])

# Attempting to modify a tuple will raise an error
# Uncommenting the following line will result in an error:
# my_tuple[0] = 10

# Concatenate tuples
tuple2 = (6, 7, 8)
concatenated_tuple = my_tuple + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Tuple unpacking
a, b, *rest = concatenated_tuple
print("Unpacked values: a =", a, ", b =", b, ", rest =", rest)

# Find the length of a tuple
tuple_length = len(concatenated_tuple)
print("Length of the Tuple:", tuple_length)

# Check if an element is present in the tuple
element_to_check = 5
if element_to_check in concatenated_tuple:
    print(f"{element_to_check} is present in the tuple.")
else:
    print(f"{element_to_check} is not present in the tuple.")
