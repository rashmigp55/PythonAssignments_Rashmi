"""
A program that executes an operation on a list and handles an IndexError exception if the index is out of range.
Input: List of integers and an index to access
Output: Value at the index or an error message if the index is invalid
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def get_element_from_list(input_list, index):
    try:
        # Attempt to access the element at the specified index
        return input_list[index]
    except IndexError:
        # Handle the case where the index is out of range
        return "Error: Index is out of range."

def main():
    # Example list
    my_list = [10, 20, 30, 40, 50]
    
    # Get user input for the index
    index = int(input("Enter the index of the element you want to access: "))
    
    # Get the element from the list or handle the exception
    result = get_element_from_list(my_list, index)
    print(result)

if __name__ == "__main__":
    main()
