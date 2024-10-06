"""
Calculate the percentage and grade of Physics, Chemistry, Biology, Mathematics, and Computer
-------------------------------------------------------------------
Code Written by:Rashmi Ganesh Patil
-------------------------------------------------------------------
"""

class myClass:
    def __init__(self,list1) -> None:
        self.list1=list1

    def calculateGrade(self) -> tuple[float, str]:
        Percent= (sum(self.list1)/500)*100
        if Percent >=90:
            grade= 'A'
        elif Percent >= 80:
            grade = 'B'
        elif Percent >= 70:
            grade = 'C'
        elif Percent >= 60:
            grade = 'D'
        elif Percent >= 40:
            grade = 'E'
        else:
            grade = 'F'
    
        return Percent, grade

def main():
    physics = int(input("Enter marks for Physics: "))
    chemistry = int(input("Enter marks for Chemistry: "))
    biology = int(input("Enter marks for Biology: "))
    math = int(input("Enter marks for Mathematics: "))
    computer = int(input("Enter marks for Computer: "))

    list1=[physics,chemistry,biology,math,computer]
    obj1=myClass(list1)
    Percentage,grade=obj1.calculateGrade()
    print("------------------------------------------------------")
    print(f"Total Percentage: {Percentage}% and grade: {grade}")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()