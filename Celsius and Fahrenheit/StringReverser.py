class StringReverser:
    def reverse_words(self, input_string):
        words = input_string.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

# Example usage
if __name__ == "__main__":
    reverser = StringReverser()
    input_str = input("Enter a string: ")

    reversed_str = reverser.reverse_words(input_str)
    print("Reversed String (word by word):", reversed_str)
