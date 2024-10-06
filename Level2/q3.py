"""
A simple program to find the number of pairs of elements in the array whose sum equals K.
Sample Input: arr = [1, 2, 3, 4, 5], k = 6
Sample Output: Pair count: 2
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def count_pairs(list1, target):
    pair_count = 0
    n = len(list1)

    # Iterate through the array and check each pair
    for i in range(n):
        for j in range(i + 1, n):  # Ensure we don't pair an element with itself
            if list1[i] + list1[j] == target:
                pair_count += 1

    return pair_count

def main():
    list1=list(map(int,input("Enter list1 separated by comma:").split(',')))# enter on command prompt:1,2,3,4,5
    target=int(input("Enter target integer:"))
    
    result = count_pairs(list1, target)
    print(f"Pair count: {result}")

if __name__ == "__main__":
    main()
