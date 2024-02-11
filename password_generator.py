import string
import random

def generate_password(length):
    """This function generates a random password
    of a given length using a combination of
    uppercase letters, lowercase letters,
    digits, and special characters"""


    # Define a string containing all possible characters
    pass_chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    # Generate a password using a random selection of characters
    for i in range(length):
        password = password + random.choice(pass_chars)
    
    strength_checker(password)


def strength_checker(password):
    """This function checks if the generated password is strong enough"""

    special_chars = string.punctuation

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True

    # Check if the password is strong enough
    if has_uppercase and has_lowercase and has_digit and has_special_char:
        print("Your Secure Password is: " + password)
    else:
        generate_password(len(password))

length = int(input("How Long do You Want Your Password to be? It Must be at Least 8 Characters. "))

while True:
    if length >= 8:
        password = generate_password(length)
        break
    else:
        length = int(input("Type a Number Greater than 8. "))

