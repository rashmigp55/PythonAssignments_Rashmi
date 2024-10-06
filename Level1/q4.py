"""
A Python program to find the sum of all odd numbers between two given numbers.
Start = 1, stop = 10 Sum of odd numbers: 25
-------------------------------------------------------------------
Code Written by:Rashmi Ganesh Patil
-------------------------------------------------------------------
"""

class myClass:
    def __init__(self,num1,num2) -> None:
        self.num1=num1
        self.num2=num2

    def checkDiv(self) -> int:
        sum=0
        for i in range(self.num1,self.num2):
            if i%2 !=0:
                sum=sum+i

        return sum

def main():
    num1=int(input("Enter the number1 startwith:"))
    num2=int(input("Enter the number2 ending:"))
    obj1=myClass(num1,num2)
    sum=obj1.checkDiv()
    print("-------------------------------------------------------------")
    print(f"sum of all odd numbers between {num1} and {num2} is: {sum}")
    print("-------------------------------------------------------------")

if __name__ == "__main__":
    main()