"""
Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the
password is incorrect give a chance to enter it again but it should not be more than 3 times.

-----------------------------------------------------------------------
Code Written by: Rashmi Ganesh Patil
-----------------------------------------------------------------------
"""

def create_account():
    username = input("Enter your username: ")
    
    # Prompt for password and re-type password
    while True:
        password = input("Enter your password: ")
        retype_password = input("Re-type your password: ")
        
        if password == retype_password:
            print(f"Account created successfully for {username}.")
            return username, password
        else:
            print("Passwords do not match. Please try again.")
            # Clear the password variables to ensure they don't hold previous values
            password = None
            retype_password = None

def login(username, correct_password):
    """Function to handle user login."""
    attempts = 0
    while attempts < 3:
        password = input("Enter your password: ")
        
        if password == correct_password:
            print("Login successful!")
            return True
        else:
            print("Incorrect password. Try again.")
            attempts += 1
            # Clear the password variable to ensure it doesn't hold the previous incorrect value
            password = None
            
    print("Too many incorrect attempts. Access denied.")
    return False

def main():
    """Main function to run the program."""
    print("*****************************************")
    print("Welcome to the Login Page")
    print("*****************************************")
    username, password = create_account()
    
    print("\nPlease log in to your account.")
    login(username, password)

if __name__ == "__main__":
    main()

