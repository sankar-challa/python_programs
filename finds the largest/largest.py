# Input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest_num = num1
elif num2 >= num1 and num2 >= num3:
    largest_num = num2
else:
    largest_num = num3

# Print the result
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_num}")
