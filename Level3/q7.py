"""
A program to construct a dictionary from the two lists containing the names of students and their corresponding
subjects. The dictionary should map the students with their respective subjects. Let’s see how to do this using for loops and
dictionary comprehension.
Input: [Sam, Alice, Mona] ,
[Commerce, Science, Computer]
Output: [Sam: Commerce, Alice: Science , Mona: Computer]
-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def main():
    students = ['Sam', 'Alice', 'Mona']
    subjects = ['Commerce', 'Science', 'Computer']

    # Method 1: Using a for loop
    student_subject_dict = {}
    for i in range(len(students)):
        student_subject_dict[students[i]] = subjects[i]

    print("Using for loop:", student_subject_dict)

    # Method 2: Using dictionary comprehension
    student_subject_dict_comp = {students[i]: subjects[i] for i in range(len(students))}

    print("Using dictionary comprehension:", student_subject_dict_comp)

if __name__ == "__main__":
    main()
