"""
A program to check if a number is a power of two using recursion.
Input: num = 16
Output: True
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def is_power_of_two(num):
    # Base case: if num is 1, it is a power of two
    if num == 1:
        return True
    # If num is less than 1, it cannot be a power of two
    elif num < 1:
        return False
    # Recursive case: check if num is even and divide by 2
    elif num % 2 == 0:
        return is_power_of_two(num // 2)
    else:
        return False

def main():
    num = int(input("Enter a number to check if it is a power of two: "))
    if is_power_of_two(num):
        print(f"{num} is a power of two.")
    else:
        print(f"{num} is not a power of two.")

if __name__ == "__main__":
    main()
