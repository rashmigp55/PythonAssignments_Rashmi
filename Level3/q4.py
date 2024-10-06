
"""
Define a class named Shape and its subclass Square. The Square class has an init function which takes length as argument. Both
classes have an area function which can print the area of the shape where Shape’s area is 0 by default.
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""
class Shape:
    def __init__(self) -> None:
        self.area1=0
    
    def area(self):
        print(f"Area of Shape is:{self.area1}")

class Square(Shape):
    def __init__(self,length) -> None:
        super().__init__()
        self.length=length
        self.area1=self.length*self.length


    def area(self):
        super().area()


def main():
    obj1 = Shape()
    obj1.area()  # This will now call the area method of the Shape class

    obj2 = Square(5)
    obj2.area()  # This will now call the area method of the Square class
    

if __name__ == "__main__":
    main()