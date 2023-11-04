# Create a string
string1 = "Hello"

# Concatenate strings
string2 = " World!"
concatenated_string = string1 + string2
print("Concatenated String:", concatenated_string)

# Accessing substrings
# Substring from index 0 to 4 (exclusive)
substring1 = concatenated_string[0:5]
print("Substring 1:", substring1)

# Substring from index 6 to the end
substring2 = concatenated_string[6:]
print("Substring 2:", substring2)

# Substring from the beginning to index 5 (exclusive)
substring3 = concatenated_string[:5]
print("Substring 3:", substring3)
