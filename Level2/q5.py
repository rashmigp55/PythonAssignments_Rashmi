"""
A program that analyzes weather data. Write a Python function that takes a list of temperature readings for a
specific location and determines the average temperature, highest temperature, and lowest temperature.
Input: temperature_readings = [25, 28, 21, 24, 27]
Output:
Average Temperature: 25.0
Highest Temperature: 28
Lowest Temperature: 21
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def analyze_temperatures(temp):

    avg_temp=sum(temp)/len(temp)
    max_temp=max(temp)
    min_temp=min(temp)

    return avg_temp,max_temp,min_temp

def main():
    temp=list(map(int,input("Enter weather data separated by comma:").split(',')))
    avg_temp, max_temp, min_temp = analyze_temperatures(temp)

        # Print the results
    print(f"Average Temperature: {avg_temp}")
    print(f"Highest Temperature: {max_temp}")
    print(f"Lowest Temperature: {min_temp}")

if __name__ == "__main__":
    main()
