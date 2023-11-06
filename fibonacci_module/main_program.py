# main_program.py
import fibonacci_module

# Get user input for the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Use the function from the imported module
fibonacci_sequence = fibonacci_module.generate_fibonacci(n)

# Print the generated Fibonacci sequence
print(f"Fibonacci sequence of {n} numbers: {fibonacci_sequence}")
