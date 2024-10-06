"""
a function that takes a list and returns a new list with unique elements of the first list.
Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
Sample Output: list2 = [1, 2, 3, 4, 5]
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------

"""

def find_unique_elements(l1):
    common_elements = list(set(l1))
    return common_elements

def main():
    l1 = list(map(int,input("Enter the list with comma separated:").split(',')))
    #l1 = list(map(int, input("Enter list1 (comma separated): ").split(',')))
    
    result = find_unique_elements(l1)
    print(f"unique elements of list are: {result}")

if __name__ == "__main__":
    main()
