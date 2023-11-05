# Create a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Dictionary:", my_dict)

# Access values using keys
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])

# Modify values
my_dict['age'] = 26
print("Modified Dictionary:", my_dict)

# Add a new key-value pair
my_dict['occupation'] = 'Engineer'
print("Dictionary after adding a new key-value pair:", my_dict)

# Remove a key-value pair
key_to_remove = 'city'
if key_to_remove in my_dict:
    removed_value = my_dict.pop(key_to_remove)
    print(f"Dictionary after removing {key_to_remove}:", my_dict)
    print(f"Removed value: {removed_value}")
else:
    print(f"{key_to_remove} not found in the dictionary.")

# Iterate through keys and values
print("Iterating through keys and values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Check if a key is present in the dictionary
key_to_check = 'name'
if key_to_check in my_dict:
    print(f"{key_to_check} is present in the dictionary.")
else:
    print(f"{key_to_check} is not present in the dictionary.")
