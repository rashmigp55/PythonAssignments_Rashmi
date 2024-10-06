"""
A program to count the number of vowels in a given string.
Input: string = "Hello, World!"
Output: Number of vowels: 3
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def count_vowels(input_string: str) -> int:
    
    vowels = "aeiouAEIOU"
    
    vowel_count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1  
            
    return vowel_count  

def main():
    string = input("Enter a string to count the number of vowels: ")
    result = count_vowels(string)
    print(f"Number of vowels: {result}")

if __name__ == "__main__":
    main()
