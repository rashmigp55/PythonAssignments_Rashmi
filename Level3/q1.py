"""
A program to read a file and return only the even length strings from the file.
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def readEvenWords(file_path):
    # Open the file
    with open(file_path,'r') as file1:
        for line in file1:
            list1=line.split(' ')
            list2=[words for words in list1 if len(words)%2 == 0]
            print(' '.join(list2))


def main():
    # file path
    file_path = 'C:\\Users\\ms365\\OneDrive\\Desktop\\Consultadd\\Python_Assignments\\Level3\\doc.txt'

    readEvenWords(file_path)

if __name__ == "__main__":
    main()
