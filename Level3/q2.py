"""
A program to read a file and return only the even length strings from the file.
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""
def countLines(file_path):
    try:
    # Open the file
        with open(file_path,'r') as file1:
            list1 = file1.readlines()#gives list of elements representing each ele as each line in a file
            print("Total number of lines in the file:",len(list1))

     
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # file path
    file_path = 'C:\\Users\\ms365\\OneDrive\\Desktop\\Consultadd\\Python_Assignments\\Level3\\doc.txt'

    countLines(file_path)

if __name__ == "__main__":
    main()
