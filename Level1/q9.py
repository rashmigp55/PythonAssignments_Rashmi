"""
A program to count the frequency of each element in a list using dict.get().
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Output: Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------

"""
class FrequencyCounter:
    def __init__(self,list1):
        self.list1=list1

    def count_frequency(self) -> dict:
        dict1={}
        for i in self.list1:
            dict1[i]=dict1.get(i,0)+1
        return dict1
    
def main():
    input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
    obj1 = FrequencyCounter(input_list)
    frequency_count = obj1.count_frequency()
    
    print("Frequency count:", frequency_count)

if __name__ == "__main__":
    main()