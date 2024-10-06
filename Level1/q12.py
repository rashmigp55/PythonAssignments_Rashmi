"""
A program to reverse a number using a while loop.
Sample Input: num = 12345
Sample Output: revnum = 54321
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------

"""

def reverse_number(num: int) -> int:
    revnum = 0
    while num > 0:
        digit = num % 10  # Get the last digit
        revnum = revnum * 10 + digit  # Append it to the reversed number
        print("revnum",revnum)
        num //= 10  # Remove the last digit from num
    return revnum

def main():
    num = int(input("Enter a number to reverse: "))
    revnum = reverse_number(num)
    print(f"revnum = {revnum}")

if __name__ == "__main__":
    main()
