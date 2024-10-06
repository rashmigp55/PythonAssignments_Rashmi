"""
Program to check if one string is an anagram of another string.
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

# Function to check if two strings are anagrams
def are_anagrams(string1: str, string2: str) -> bool:
    # Remove spaces and convert to lowercase for comparison
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    
    # Sort the characters and compare
    return sorted(string1) == sorted(string2)

def main():
    # Define two strings
    string1 = "listen"
    string2 = "silent"

    # Check and print if they are anagrams
    if are_anagrams(string1, string2):
        print(f"{string1} and {string2} are anagrams: True")
    else:
        print(f"{string1} and {string2} are anagrams: False")

if __name__ == "__main__":
    main()
