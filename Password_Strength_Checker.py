import re

def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return "Password is too short. Must be at least 8 characters."
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password should contain at least one uppercase letter."
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase letter."
    
    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return "Password should contain at least one number."
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should contain at least one special character."
    
    return "Password is strong."

# Loop until a strong password is entered
while True:
    password = input("Enter your password: ")
    result = check_password_strength(password)
    
    if result == "Password is strong.":
        print(result)
        break  # Exit the loop once the password is strong
    else:
        print(result)  # Display the error message
