"""
A program in Python to perform the following operation:

If a number is divisible by 3 it should print “Consultadd” as a
string
If a number is divisible by 5 it should print “Python Training” as
a string
If a number is divisible by both 3 and 5 it should print
“Consultadd - Python Training” as a string.
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------

"""
class myClass:
    def __init__(self,num) -> None:
        self.num=num

    def checkDiv(self) -> None:
        if self.num%5==0 & self.num%3==0:
            print("Consultadd - Python Training")
        elif self.num % 3 ==0:
            print("Consultadd")
        
        elif self.num % 5 ==0:
             print("Python Training")
        else:
            print("Entered number is neither divisible by 3 not 5")

def main():
    num1=int(input("Enter number to check if divisible by 3 or 5 or both:"))
    obj1=myClass(num1)
    obj1.checkDiv()

if __name__ == "__main__":
    main()