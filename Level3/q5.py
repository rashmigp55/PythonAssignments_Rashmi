"""
Create a class 'Time' and initialize it with hours and minutes. Create a method addTime() which should take two Time objects
and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

class Time:
    def __init__(self,hour,minutes) -> None:
        self.hour=hour
        self.minutes=minutes


    def addTime(self,newObj):
        self.hour=self.hour+newObj.hour
        self.minutes=self.minutes+newObj.minutes
        if self.minutes >=60:
            totalHour=self.hour+(self.minutes//60)
            totalMinutes=self.minutes%60
        return Time(totalHour,totalMinutes)
    
    def displayTime(self):
         print(f"\t{self.hour} hr and {self.minutes} min")

    def displayMinute(self):
        """Display the total minutes in the Time object."""
        total_minutes = self.hour * 60 + self.minutes
        print(f"\tTotal minutes: {total_minutes} minute(s)")

        
def main():
    obj1=Time(2,50)
    obj2=Time(1,20)
    obj3=obj1.addTime(obj2)
    print("------------------------------------------------------------------------------")
    obj3.displayTime()
    obj3.displayMinute()
    print("------------------------------------------------------------------------------")

    

if __name__ == "__main__":
    main()