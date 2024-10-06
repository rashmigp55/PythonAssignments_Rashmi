"""
Program to calculate the LCM (Least Common Multiple) of two numbers.
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""
class myClass:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def gcd(self) -> int:
        n=min(self.a,self.b)
        for i in range(1,n):
            if self.a%i ==0 & self.b%i==0:
                gcd=i
        return gcd


def main():
    num1=int(input("Enter number1:"))
    num2=int(input("Enter number2:"))

    obj1=myClass(num1,num2)
    gcd_value=obj1.gcd()

    lcm=(num1*num2)//gcd_value

    # Print the result
    print(f"GCD of {num1} and {num2} is: {lcm}")

if __name__ == "__main__":
    main()
