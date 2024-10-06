"""
A program to find if a given string starts with a given character using a lambda function.
Input: input_string = "Hello, World!", given_char = "H"
Output: True
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def starts_with(input_string, given_char):
    # Using a lambda function to check if the string starts with the given character
    check_start = lambda s, c: s.startswith(c)
    return check_start(input_string, given_char)

def main():
    input_string = "Hello, World!"
    given_char = "H"
    
    result = starts_with(input_string, given_char)
    if result:
        print("***********************************************************\n")
        print(f"\t\tYes string startswith {given_char}\n")
        print("***********************************************************\n")
    else:
        print("***********************************************************\n")
        print(f"\t\tString does not startswith {given_char}\n")
        print("***********************************************************\n")

if __name__ == "__main__":
    main()
