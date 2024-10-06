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

def parse_encoded_string(encoded_string):
    # Split the string by '0'
    parts = encoded_string.split('0')
    
    # Initialize an empty list to hold non-empty parts
    non_empty_parts = []
    
    # Loop through the parts and append non-empty ones to the list
    for part in parts:
        if part:  # Check if the part is not an empty string
            non_empty_parts.append(part)
    
    # Create a dictionary with the appropriate keys
    result = {
        "first_name": non_empty_parts[0],  # First part is the first name
        "last_name": non_empty_parts[1],   # Second part is the last name
        "id": non_empty_parts[2]           # Third part is the ID
    }
    
    return result
def main():
    input_string = "Robert000Smith000123"
    output = parse_encoded_string(input_string)
    print(output)

if __name__ == "__main__":
    main()