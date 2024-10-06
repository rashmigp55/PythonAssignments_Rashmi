"""
 Aditi has used text editing software to type some text. After saving the article as words.txt, she realized that she had wrongly
typed the alphabet “J" instead of “I" everywhere in the article. Write a function definition for JtoI() in Python that would display
the corrected version of the entire content of the file WORDS.TXT with all the alphabet "J" to be displayed as an alphabet "I" on the
screen.Note: Assume that words.txt does not contain any J alphabet otherwise.
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""
def Jtol(filePath):
    try:
        with open(filePath,'r') as file1:
            fileContent=file1.read()
            replacedContent=fileContent.replace('J','I')
            print(replacedContent)

    except FileNotFoundError:
        print(f"Error:file {filePath} was not found")
    
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # file path
    file_path = 'C:\\Users\\ms365\\OneDrive\\Desktop\\Consultadd\\Python_Assignments\\Level3\\words.txt'

    Jtol(file_path)

if __name__ == "__main__":
    main()