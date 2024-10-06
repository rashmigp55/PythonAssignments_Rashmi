"""
A Python program to find the factorial of a number using a for loop.
-------------------------------------------------------------------
Code Written by:Rashmi Ganesh Patil
-------------------------------------------------------------------
"""
class myWork:
    def isFactorial(self,num1):
        self.result=num1
        for num2 in range(num1-1,0,-1):
            
            self.result=self.result*num2
        return self.result
      

def main():
    num1=int(input("Please enter the number to find the factorial:"))

  
    obj1=myWork()
    result=obj1.isFactorial(num1)
   
    
    print("Factorial of number",num1,"is:",result)
   



if __name__ == '__main__':
    main()