class PowerCalculator:
    def power(self, x, n):
        if n < 0:
            return 1 / self.power_positive(x, -n)
        else:
            return self.power_positive(x, n)

    def power_positive(self, x, n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            half_pow = self.power_positive(x, n // 2)
            return half_pow * half_pow
        else:
            half_pow = self.power_positive(x, (n - 1) // 2)
            return x * half_pow * half_pow

# Example usage
if __name__ == "__main__":
    calculator = PowerCalculator()
    base = float(input("Enter the base (x): "))
    exponent = int(input("Enter the exponent (n): "))

    result = calculator.power(base, exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")
