# copyfile.py

# Prompt the user for file names
input_file_name = input("Enter the name of the input text file: ")
output_file_name = input("Enter the name of the output text file: ")

# Read the contents of the input file
try:
    with open(input_file_name, 'r') as input_file:
        file_contents = input_file.read()
except FileNotFoundError:
    print(f"Error: File '{input_file_name}' not found.")
    exit()

# Write the contents to the output file
with open(output_file_name, 'w') as output_file:
    output_file.write(file_contents)

print(f"Contents of '{input_file_name}' have been copied to '{output_file_name}'.")
