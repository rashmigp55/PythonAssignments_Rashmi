"""
A program to calculate the sum of digits of a given number until
the sum becomes a single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24
Final Output: 6
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------

"""

def sum_of_digits(num: int) -> int:
    while num >= 10:
        total_sum = 0        
        while num > 0:             
            dig = num % 10
            print(dig)  # Print the digit being processed
            total_sum += dig
            num //= 10  # Use integer division to discard the last digit
        print("\n**sum", total_sum)
        num = total_sum  # Update num to the sum of its digits
    return num  # Return the final single-digit result

def main():
    num = int(input("Enter number to find sum of digits: "))
    final_output = sum_of_digits(num)
    print("=================================================================")
    print(f"Final Output: {final_output}")
    print("=================================================================")

if __name__ == "__main__":
    main()
