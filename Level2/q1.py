"""
A program to find the common elements between two lists.
Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
Sample Output: [4, 5]
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------

"""

def find_common_elements(l1, l2):
    common_elements = list(set(l1) & set(l2))
    return common_elements

def main():
    l1 = list(map(int, input("Enter list1 (comma separated): ").split(',')))
    l2 = list(map(int, input("Enter list2 (comma separataed): ").split(',')))
    
    result = find_common_elements(l1, l2)
    print(f"Common elements: {result}")

if __name__ == "__main__":
    main()
