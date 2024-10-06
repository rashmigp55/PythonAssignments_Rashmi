"""
Given an input string, write a function that returns the run length encoded string for the input string.
For Example:
Input: wwwwaaadebbbbbw
Output: w4a3d1e1b5w1

-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def encode(string1):
    if not string1:
        return ""

    encodedString = ""
    count = 1

    for i in range(1, len(string1)):
        if string1[i] == string1[i - 1]:
            count += 1
        else:
            encodedString += string1[i - 1] + str(count)
            print(encodedString)
            count = 1

    encodedString += string1[-1] + str(count)
    return encodedString

def main():
   input_string = "wwwwaaadebbbbbw"
   output = encode(input_string)
   print("-------------------------------------------")
   print("\tfinal output:",output)  # Output: w4a3d1e1b5w1
   print("-------------------------------------------")

if __name__ == "__main__":
    main()