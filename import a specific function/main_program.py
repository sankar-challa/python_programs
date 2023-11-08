# main_program.py
from math_operations import multiply

# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Use the imported function
result = multiply(num1, num2)

# Print the result
print(f"The product of {num1} and {num2} is: {result}")
