def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Get user choice
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
choice = int(input("Enter your choice (1 or 2): "))

# Perform the conversion based on user choice
if choice == 1:
    celsius_temp = float(input("Enter temperature in Celsius: "))
    converted_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp} Celsius is equal to {converted_temp:.2f} Fahrenheit.")
elif choice == 2:
    fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
    converted_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp} Fahrenheit is equal to {converted_temp:.2f} Celsius.")
else:
    print("Invalid choice. Please enter 1 or 2.")
