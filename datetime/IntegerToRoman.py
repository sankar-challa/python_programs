class IntegerToRoman:
    def __init__(self):
        # Define the Roman numeral symbols and their corresponding values
        self.symbols = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1)
        ]

    def convert_to_roman(self, num):
        if not isinstance(num, int) or not (0 < num < 4000):
            raise ValueError("Input must be an integer between 1 and 3999.")

        result = ''
        for symbol, value in self.symbols:
            while num >= value:
                result += symbol
                num -= value

        return result

# Example usage
if __name__ == "__main__":
    converter = IntegerToRoman()
    number_to_convert = int(input("Enter an integer (1 to 3999): "))
    
    try:
        roman_numeral = converter.convert_to_roman(number_to_convert)
        print(f"The Roman numeral for {number_to_convert} is: {roman_numeral}")
    except ValueError as e:
        print(e)
