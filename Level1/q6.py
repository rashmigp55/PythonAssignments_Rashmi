"""
Program to check if a given number is a perfect number.
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

# Function to check if a number is a perfect number
def is_perfect_number(number) -> bool:
    # Initialize sum of divisors
    sum_of_divisors = 0

    # Find all divisors of the number except the number itself
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    
    # Check if sum of divisors is equal to the number
    return sum_of_divisors == number

def main():
    # Input a number from the user
    number = int(input("Enter a number to check if it's a perfect number: "))

    # Check and print if the number is perfect or not
    if is_perfect_number(number):
        print(f"Yes, {number} is a perfect number.")
    else:
        print(f"No, {number} is not a perfect number.")

if __name__ == "__main__":
    main()
