"""
a program that accepts a string as input from the user and calculates the number of digits and letters.
Input: Hello123
Output: Alphabets: 5 & Number : 3
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------

"""
class myClass:
    def __init__(self,myString:str) -> None:
        self.myString=myString

    def check(self) -> None:
        chars=0
        numbers=0
        for ch in self.myString:
            if ch.isalpha():
                chars+=1
            elif ch.isdigit():
                numbers+=1

        print(f"characters={chars} and digits={numbers}")

def main():
    string1=input("Please enter the string to check alphabets ans numbers:")
    obj1=myClass(string1)
    obj1.check()


if __name__ == "__main__":
    main()