"""
Write a Python program to create a list of given strings individually of the list using the Python map function.
Eg. Input:
['Red', 'Blue', 'Black', 'White', 'Pink']
Output:
[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i',
'n', 'k']]
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def main():
    # Input list of strings
    input_list = ['Red', 'Blue', 'Black', 'White', 'Pink']
    
    # Use map to apply the string_to_char_list function to each element in the input list
    output = list(map(list, input_list))
    
    # Print the output
    print(output)

if __name__ == "__main__":
    main()
