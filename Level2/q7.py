"""
A Python function that finds the median of a list of numbers.
Sample Input: number_list = [7, 2, 5, 1, 9, 3]
Sample Output: Median: 4.0
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""
def find_median(list1):
    rem=len(list1)%2
    sortedList=sorted(list1)
    if  rem==1:
        return sortedList[len(list1)//2]
    else:
        midNum1=sortedList[len(list1)//2-1]
        midNum2=sortedList[len(list1)//2]
        print(midNum1)
        print(midNum2)
        return (midNum1+midNum2)/2

def main():
    number_list = [7, 2, 5, 1, 9, 3]  # Sample input
    list1=list(map(int,input("Enter list to find median separated by comma:").split(',')))
    median = find_median(list1)
    print(f"Median: {median}")

if __name__ == "__main__":
    main()