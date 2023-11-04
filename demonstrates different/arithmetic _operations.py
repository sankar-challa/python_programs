# Input numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
sum_result = num1 + num2
print("Sum:", sum_result)

# Subtraction
difference_result = num1 - num2
print("Difference:", difference_result)

# Multiplication
product_result = num1 * num2
print("Product:", product_result)

# Division
if num2 != 0:
    quotient_result = num1 / num2
    print("Quotient:", quotient_result)
else:
    print("Cannot divide by zero.")

# Modulus (remainder)
if num2 != 0:
    modulus_result = num1 % num2
    print("Modulus:", modulus_result)
else:
    print("Cannot calculate modulus with zero divisor.")

# Exponentiation
exponent_result = num1 ** num2
print("Exponentiation:", exponent_result)
