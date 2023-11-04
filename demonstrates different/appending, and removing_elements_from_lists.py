# Create a list
my_list = [1, 2, 3, 4, 5]
print("Initial List:", my_list)

# Append elements to the list
my_list.append(6)
my_list += [7, 8]
print("List after Appending Elements:", my_list)

# Remove element by value
value_to_remove = 3
if value_to_remove in my_list:
    my_list.remove(value_to_remove)
    print(f"List after Removing {value_to_remove}:", my_list)
else:
    print(f"{value_to_remove} not found in the list.")

# Remove element by index
index_to_remove = 2
if 0 <= index_to_remove < len(my_list):
    removed_element = my_list.pop(index_to_remove)
    print(f"List after Removing Element at Index {index_to_remove}:", my_list)
    print(f"Removed Element: {removed_element}")
else:
    print(f"Index {index_to_remove} is out of range.")

# Clear the entire list
my_list.clear()
print("List after Clearing:", my_list)
