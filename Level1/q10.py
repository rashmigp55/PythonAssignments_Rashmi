"""
A program to reverse the order of words in a given sentence.
Input_sentence = "Hello, World! Welcome to Python programming."
Output after reverse = "programming. Python to Welcome World! Hello,"
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------

"""

def reverse_words(sentence: str) -> str:
    # Split the sentence into words using split() method
    words = sentence.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list back into a string
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

def main():
    input_sentence = "Hello, World! Welcome to Python programming."
    output_sentence = reverse_words(input_sentence)
    print("Output after reverse =", output_sentence)

if __name__ == "__main__":
    main()
