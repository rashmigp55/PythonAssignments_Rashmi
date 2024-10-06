"""
an array of size N. The task is to rotate array by D elements towards right
Sample Input: arr = [1, 2, 3, 4, 5], D = 2
Sample Output: arr after rotation = [4, 5, 1, 2, 3]
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def rotateRight(list1, D):

    return list1[-D:]+list1[:-D]

def main():
    list1=list(map(int,input("Enter list1 separated by comma:").split(',')))# enter on command prompt:1,2,3,4,5
    rotateBy=int(input("Rotate by(enter int):"))
    
    newList = rotateRight(list1, rotateBy)
    print(f"After rotating list: {newList}")

if __name__ == "__main__":
    main()
